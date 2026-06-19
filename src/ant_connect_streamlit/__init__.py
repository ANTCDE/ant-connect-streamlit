from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal, NotRequired, TypedDict
from uuid import uuid4

import streamlit as st

from ant_connect_streamlit._bridge import render_bridge
from ant_connect_streamlit.models import Context, License, ProjectShort, Signal, Task, User

NotificationType = Literal["success", "error", "warning", "info"]


class RequestOptions(TypedDict, total=False):
    method: Literal["get", "post", "put", "patch", "delete"]
    data: Any
    params: dict[str, str]
    headers: dict[str, str]


class ResponseConfig(TypedDict, total=False):
    type: type
    onSuccess: Callable[[Any], None]
    onError: Callable[[str], None]


class PendingRequest:
    """Returned by ``AntConnect.request()``. Chain ``.response()`` to handle the result."""

    def __init__(self, raw: Any | None = None, resolved: bool = False) -> None:
        self._raw = raw
        self._resolved = resolved

    def response(self, config: ResponseConfig | None = None) -> Any | None:
        if not self._resolved:
            return None
        cfg = config or {}
        raw = self._raw
        if isinstance(raw, dict) and "error" in raw and len(raw) == 1:
            on_error = cfg.get("onError")
            if on_error:
                on_error(raw["error"])
            return raw
        model = cfg.get("type")
        result = model.model_validate(raw) if model and hasattr(model, 'model_validate') else raw
        on_success = cfg.get("onSuccess")
        if on_success:
            on_success(result)
        return result


class ToolbarMenuItem(TypedDict):
    icon: str
    title: str
    notify: NotRequired[str]
    notifyType: NotRequired[NotificationType]
    action: NotRequired[str]
    disabled: NotRequired[bool]


__all__ = [
    "connect", "AntConnect", "RequestOptions", "ResponseConfig", "PendingRequest", "ToolbarMenuItem",
    "Context", "User", "License", "ProjectShort", "Task", "Signal",
]

_LIMITS_KEYS = ("limits",)


def _fix_empty_arrays_to_dicts(data: Any, depth: int = 0) -> None:
    if depth > 10 or not isinstance(data, dict):
        return
    for key, value in data.items():
        if key in _LIMITS_KEYS and isinstance(value, list) and len(value) == 0:
            data[key] = {}
        elif isinstance(value, dict):
            _fix_empty_arrays_to_dicts(value, depth + 1)


class AntConnect:
    """Per-session bridge between a Streamlit app and the ANT-OS host.

    Obtain via ``ant_connect.connect()`` at the top of your script.
    The instance is cached in ``st.session_state`` and reused across reruns.
    """

    _SESSION_KEY = "_ant_connect_instance"

    def __init__(self) -> None:
        self._context: Context | None = None
        self._prev_context: Context | None = None
        self._signals: list[dict] = []
        self._requests: list[dict] = []
        self._responses: dict[str, Any] = {}
        self._pending: set[str] = set()
        self._req_id_map: dict[str, str] = {}
        self._received_signals: list[dict] = []
        self._signals_to_ack: int = 0
        self._subscriptions: dict[str, dict] = {}

    @property
    def context(self) -> Context | None:
        return self._context

    @property
    def context_changed(self) -> bool:
        return self._context != self._prev_context

    def changed(self, *fields: str) -> bool:
        """Check if specific context fields changed since last run.

        With no args, equivalent to ``context_changed``.
        """
        if not fields:
            return self.context_changed
        for field in fields:
            prev = getattr(self._prev_context, field, None) if self._prev_context else None
            curr = getattr(self._context, field, None) if self._context else None
            if prev != curr:
                return True
        return False

    @property
    def user(self) -> User | None:
        return self._context.user if self._context else None

    @property
    def project(self) -> ProjectShort | None:
        return self._context.project if self._context else None

    @property
    def task(self) -> Task | None:
        return self._context.selected_task if self._context else None

    @property
    def dark_mode(self) -> bool | None:
        return self._context.dark_mode if self._context else None

    def send_signal(self, payload: dict | Signal, *, rerun: bool = True) -> None:
        """Queue a signal for the ANT-OS host.

        Accepts a raw dict or a typed ``Signal`` model instance.
        By default triggers ``st.rerun()`` so the signal is delivered
        immediately on the next ``connect()`` call.  Pass ``rerun=False``
        to batch multiple signals before a manual ``st.rerun()``.
        """
        if isinstance(payload, Signal):
            payload = payload.model_dump(by_alias=True, exclude_none=True)
        nonce = str(uuid4())
        self._signals.append({"nonce": nonce, "payload": payload})

        if rerun:
            st.rerun()

    def call_service(self, service: str, method: str, args: list | None = None) -> Any | None:
        """Call an ANT-OS host service.

        First call queues the request and returns ``None``.  On a
        subsequent rerun the cached response is returned.
        """
        import json
        cache_key = f"{service}.{method}.{json.dumps(args or [], sort_keys=True, default=str)}"
        if cache_key in self._responses:
            return self._responses[cache_key]
        if cache_key not in self._pending:
            self._pending.add(cache_key)
            self._requests.append({
                "id": cache_key,
                "service": service,
                "method": method,
                "args": args or [],
            })
        return None

    def clear_request_cache(self) -> None:
        """Clear all cached HTTP responses so requests can be re-fetched."""
        self._responses.clear()
        self._pending.clear()
        self._requests.clear()
        self._req_id_map.clear()

    def request(self, url: str, options: RequestOptions | None = None) -> PendingRequest:
        """Make an HTTP request through the host's authenticated Axios instance.

        Returns a ``PendingRequest``. Chain ``.response()`` to handle the result::

            ant.request("/api/projects").response({"type": ProjectShort, "onSuccess": lambda d: ...})

        The host adds auth headers automatically. First rerun queues the request,
        subsequent rerun returns cached data through ``.response()``.
        """
        import json
        opts = options or {}
        method = opts.get("method", "get")
        params = opts.get("params")
        cache_key = f"_req.{method}.{url}.{json.dumps(params or {}, sort_keys=True, default=str)}"
        if cache_key in self._responses:

            return PendingRequest(self._responses[cache_key], resolved=True)
        if cache_key not in self._pending:
            req_id = f"{cache_key}.{uuid4().hex[:8]}"
            self._pending.add(cache_key)
            self._req_id_map[req_id] = cache_key
            self._requests.append({
                "id": req_id,
                "type": "http",
                "url": url,
                "method": method,
                "data": opts.get("data"),
                "params": params,
                "headers": opts.get("headers"),
            })
            st.rerun()
        return PendingRequest()

    def set_toolbar(
        self,
        *,
        title: str | None = None,
        subtitle: str | None = None,
        loading: bool | None = None,
        menu: list[ToolbarMenuItem] | None = None,
    ) -> None:
        """Set the host toolbar title, subtitle, loading, or menu items.

        Menu items: ``[{"icon": "mdi-refresh", "title": "Refresh", "notify": "Done!", "notifyType": "success"}]``
        """
        update: dict[str, Any] = {}
        if title is not None:
            update["title"] = title
        if subtitle is not None:
            update["subtitle"] = subtitle
        if loading is not None:
            update["isLoading"] = loading
        if menu is not None:
            update["menu"] = menu
        if update:

            nonce = str(uuid4())
            self._signals.append({"nonce": nonce, "payload": {"_toolbar": update}})

    def notify(self, message: str, *, type: NotificationType = "info", rerun: bool = True) -> None:
        """Show a toast notification on the ANT-OS host."""

        nonce = str(uuid4())
        self._signals.append({"nonce": nonce, "payload": {"_notify": {"type": type, "message": message}}})
        if rerun:
            st.rerun()

    def events(self, kind: str | None = None) -> list[dict]:
        """Return and drain accumulated signal events from the host.

        Pass a signal key (e.g. ``"task"``, ``"topic"``, ``"limitChange"``)
        to filter, or ``None`` for all events.
        """
        if kind is None:
            result = self._received_signals[:]
            self._received_signals.clear()
            return result
        matched = [s for s in self._received_signals if kind in s]
        self._received_signals = [s for s in self._received_signals if kind not in s]
        return matched

    def observe(self, entity_type: str, entity_id: str | None = None,
                actions: list[str] | None = None) -> str:
        """Start observing entity changes via Echo. Returns key for ``unobserve()``."""
        random = str(uuid4())
        sub_key = f"observe:{random}"
        self._subscriptions[sub_key] = {"type": "observe", "random": random}
        payload: dict[str, Any] = {"observe": {"random": random, "type": entity_type}}
        if entity_id is not None:
            payload["observe"]["id"] = entity_id
        if actions is not None:
            payload["observe"]["actions"] = actions
        self.send_signal(payload, rerun=False)
        return sub_key

    def unobserve(self, sub_key: str) -> None:
        """Stop observing an entity previously registered with ``observe()``."""
        sub = self._subscriptions.pop(sub_key, None)
        if sub and sub["type"] == "observe":
            self.send_signal({"unobserve": {"random": sub["random"]}}, rerun=False)

    def subscribe_channel(self, channel: str, events: list[str]) -> str:
        """Subscribe to an Echo channel. Events arrive via ``events()``."""
        sub_key = f"channel:{channel}"
        self._subscriptions[sub_key] = {"type": "channel", "channel": channel}
        self.send_signal({"subscribeChannel": {"channel": channel, "events": events}}, rerun=False)
        return sub_key

    def unsubscribe_channel(self, channel: str) -> None:
        """Unsubscribe from an Echo channel."""
        self._subscriptions.pop(f"channel:{channel}", None)
        self.send_signal({"unsubscribeChannel": {"channel": channel}}, rerun=False)

    def publish_topic(self, name: str, data: Any = None, scope: str = "project") -> None:
        """Publish a message to a topic. Other apps receive via ``events("topic")``."""
        self.send_signal({"topic": {"name": name, "data": data, "scope": scope}}, rerun=False)

    def _sync(self) -> None:
        self._prev_context = self._context
        signals = self._signals[:]
        self._signals.clear()
        ack = self._signals_to_ack
        self._signals_to_ack = 0
        raw = render_bridge(signals=signals, requests=self._requests, ack_signals=ack)

        if raw and isinstance(raw, dict):
            msg_type = raw.get("type")
            if msg_type == "context" and "data" in raw:
                _fix_empty_arrays_to_dicts(raw["data"])
                self._context = Context.model_validate(raw["data"])
            elif msg_type == "response":
                resp_id = raw["id"]
                cache_key = self._req_id_map.pop(resp_id, resp_id)
                if cache_key not in self._responses:
                    self._responses[cache_key] = (
                        raw.get("data") if "data" in raw else {"error": raw.get("error")}
                    )
                    self._pending.discard(cache_key)
                    self._requests.clear()

            incoming = raw.get("signals", [])
            if incoming:
                self._received_signals.extend(incoming)
                self._signals_to_ack = len(incoming)


def connect() -> AntConnect:
    """Initialize the ANT-OS bridge.  Call once at the top of your script."""
    key = AntConnect._SESSION_KEY
    if key not in st.session_state:
        st.session_state[key] = AntConnect()
    ant: AntConnect = st.session_state[key]
    ant._sync()
    return ant


