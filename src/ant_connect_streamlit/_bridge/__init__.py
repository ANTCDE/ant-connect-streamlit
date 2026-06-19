from pathlib import Path

import streamlit.components.v1 as components

_frontend_dir = Path(__file__).parent / "frontend" / "dist"
_component = components.declare_component("ant_connect_bridge", path=str(_frontend_dir))


def render_bridge(
    key: str = "ant_connect_bridge",
    signals: list | None = None,
    requests: list | None = None,
    ack_signals: int = 0,
) -> dict | None:
    return _component(key=key, default=None, signals=signals or [], requests=requests or [], ack_signals=ack_signals)
