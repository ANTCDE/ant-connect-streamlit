# ant-connect-streamlit

Python/Streamlit bridge for ANT-OS iframe communication. Typed Pydantic v2 models auto-generated from TypeScript source.

## Architecture

```
ANT-OS host (Vue)
  ↕ Comlink over MessagePort
Bridge iframe (src/ant_connect_streamlit/_bridge/frontend/)
  ↕ Streamlit component protocol (setComponentValue / render args)
Python ant_connect_streamlit.connect()
```

- **JS → Python**: `client.context.subscribe()` → `Streamlit.setComponentValue()`
- **Python → JS**: `send_signal()` queues in session state → `args.signals` on render → bridge dedupes by nonce → `client.signal.send()`
- **HTTP proxy**: Python queues request → bridge `client.request()` → host Axios (authed) → response via `setComponentValue`

## Package structure

```
src/ant_connect_streamlit/
  __init__.py     # Public API: connect(), AntConnect, types
  models.py       # AUTO-GENERATED Pydantic v2 models (do not edit)
  py.typed        # PEP 561 marker
  _bridge/
    __init__.py   # render_bridge() — Streamlit custom component
    frontend/     # Vite TS project bundling @antcde/connect-ts
      dist/       # Built output (committed, served by Streamlit)
```

## Commands

```bash
uv sync                              # Install deps
uv run streamlit run app.py           # Run demo (from demo repo)

# Rebuild bridge JS (after TS changes)
cd src/ant_connect_streamlit/_bridge/frontend && npm run build

# Regenerate Python types (from ant-connect-ts)
cd ../../ant-connect-ts && pnpm run generate:python-types
```

## Key patterns

- `connect()` caches instance in `st.session_state`, calls `_sync()` on every rerun
- Signals queue → deliver on next `render_bridge()` call → bridge JS forwards to host
- `_toolbar`/`_notify`/`_action` prefixed payloads are intercepted by bridge, not forwarded as signals
- HTTP requests use unique IDs per attempt (`cache_key.uuid_hex`) to prevent bridge dedup blocking re-fetches
- Response replay guard: `if cache_key not in self._responses`
