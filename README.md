# ant-connect-streamlit

Python bridge for building Streamlit apps that run inside ANT-OS. Provides typed access to host context, signals, notifications, toolbar control, and an authenticated HTTP proxy.

## Install

```bash
pip install ant-connect-streamlit
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add ant-connect-streamlit
```

## Quick start

```python
import streamlit as st
import ant_connect_streamlit as ant

bridge = ant.connect()

if bridge.context is None:
    st.info("Waiting for ANT-OS context...")
    st.stop()

st.write(f"Hello {bridge.user.firstname}!")
st.write(f"Project: {bridge.project.name}")
```

Run with `streamlit run app.py` and load in ANT-OS via Developer mode at `/developer/8501`.

## API

### `connect() -> AntConnect`

Initialize the bridge. Call once at the top of your script. The instance is cached in `st.session_state` and reused across Streamlit reruns.

### Context

```python
bridge.context      # Full Context object (typed)
bridge.user         # User | None
bridge.project      # ProjectShort | None
bridge.task         # Task | None
bridge.dark_mode    # bool | None
bridge.context_changed  # True if context changed since last rerun
bridge.changed("project", "user")  # Check specific fields
```

### Signals

Send signals to the ANT-OS host:

```python
# Raw dict
bridge.send_signal({"navigate": {"to": "OS.dash"}})
bridge.send_signal({"notepad": {"action": "toggle"}})
bridge.send_signal({"overlay": {"action": True}})

# Navigate to app
bridge.send_signal({"navigate": {"to": {"app": {"id": "my-app-id"}}}})

# Typed Signal model
from ant_connect_streamlit import Signal
bridge.send_signal(Signal(navigate={"to": "OS.profile"}))
```

### Notifications

```python
bridge.notify("Saved!", type="success")
bridge.notify("Something went wrong", type="error")
bridge.notify("Check your input", type="warning")
bridge.notify("FYI: task updated", type="info")
```

### Toolbar

```python
bridge.set_toolbar(
    title="My App",
    subtitle="v1.0",
    loading=True,
    menu=[
        {"icon": "mdi-refresh", "title": "Refresh", "notify": "Refreshed!"},
        {"icon": "mdi-counter", "title": "Count", "action": "increment_title"},
    ],
)
```

### HTTP proxy

Make authenticated requests through the host:

```python
result = bridge.request("/api/projects").response({
    "type": ProjectShort,
    "onSuccess": lambda d: ...,
    "onError": lambda e: ...,
})
```

The host adds authentication headers automatically. Requests are cached per URL+params — call `bridge.clear_request_cache()` to re-fetch.

### Service calls

Call host services directly:

```python
data = bridge.call_service("tables", "getAll", [project_id])
```

## Types

All models are auto-generated from the ANT-OS TypeScript types and ship as Pydantic v2 models:

```python
from ant_connect_streamlit import (
    Context, User, License, ProjectShort, Task, Signal,
    RequestOptions, ResponseConfig, ToolbarMenuItem,
)
```

The package includes a `py.typed` marker for PEP 561 — IDEs get full autocomplete and type checking.

## Requirements

- Python >= 3.11
- Streamlit >= 1.30.0
- ANT-OS host (the app runs inside an ANT-OS iframe)

## Architecture

```
ANT-OS host (Vue)
  ↕ Comlink over MessagePort
Bridge iframe (bundled JS)
  ↕ Streamlit component protocol
Your Python app
```

The bridge component is a Streamlit custom component that establishes a Comlink connection to the ANT-OS host. Context flows from host to Python, signals flow from Python to host, HTTP requests are proxied through the host's authenticated Axios instance.

## Demo

See [ant-connect-streamlit-demo](https://github.com/ANTCDE/ant-connect-streamlit-demo) for a full working example.
