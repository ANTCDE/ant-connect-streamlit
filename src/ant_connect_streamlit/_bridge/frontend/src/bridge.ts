import type { Client, Signal } from '@antcde/connect-ts'
import { newCommsClient } from '@antcde/connect-ts'
import { distinctUntilChanged } from 'rxjs'

// --- Streamlit Component Protocol (raw postMessage, no React dependency) ---

function stSetReady() {
  window.parent.postMessage({ isStreamlitMessage: true, type: 'streamlit:componentReady', apiVersion: 1 }, '*')
}

function stSetValue(value: unknown) {
  window.parent.postMessage({ isStreamlitMessage: true, type: 'streamlit:setComponentValue', value }, '*')
}

function stSetHeight(height: number) {
  window.parent.postMessage({ isStreamlitMessage: true, type: 'streamlit:setFrameHeight', height }, '*')
}

// --- Port Relay for nested iframe ---
// Window A = ANT-OS host        → runs newCommsHost, expects Comlink protocol
// Window B = Streamlit iframe    → same-origin as C, no ant-connect code
// Window C = Component iframe    → this bridge
//
// Host posts ant-comms-init (with MessagePort) to Window B and listens for
// ant-comms-ready from Window B. We relay both through Window B:
//   - Intercept ant-comms-init on parent (same-origin listener) → forward port to self
//   - Inject script into parent so ant-comms-ready forwards with event.source = Window B

function installRelay(): boolean {
  const hostWindow = window.top
  if (!hostWindow || hostWindow === window.parent) {
    console.warn('[ant-connect] not nested in ANT-OS host (top === parent)')
    return false
  }

  window.parent.addEventListener('message', (event: MessageEvent) => {
    if (event.data?.type === 'ant-comms-init' && event.ports?.length > 0)
      window.postMessage(event.data, '*', [...event.ports])
  })

  try {
    const parentDoc = window.parent.document
    if (!parentDoc.querySelector('[data-ant-relay]')) {
      const script = parentDoc.createElement('script')
      script.setAttribute('data-ant-relay', '')
      script.textContent = `
        window.addEventListener('message', function(event) {
          if (event.data && event.data.type === 'ant-comms-ready' && event.source && event.source !== window) {
            window.parent.postMessage(event.data, '*');
          }
        });
      `
      parentDoc.head.appendChild(script)
    }
  }
  catch (e) {
    console.warn('[ant-connect] relay: could not inject script (cross-origin?)', e)
    return false
  }

  return true
}

// --- Signal Bridge (Python → ANT-OS) ---

let client: Client | null = null
const sentSignals = new Set<string>()
let pendingSignals: Array<{ nonce: string, payload: Record<string, unknown> }> = []
const state = { titleCount: 0 }

function flushSignals() {
  if (!client || !pendingSignals.length)
    return
  const batch = pendingSignals
  pendingSignals = []
  for (const sig of batch) {
    if (sentSignals.has(sig.nonce))
      continue
    sentSignals.add(sig.nonce)
    client.signal.send(sig.payload as Signal)
  }
}

function handleSignals(signals?: Array<{ nonce: string, payload: Record<string, unknown> }>) {
  if (!signals?.length)
    return
  if (!client) {
    pendingSignals.push(...signals)
    return
  }
  flushSignals()
  for (const sig of signals) {
    if (sentSignals.has(sig.nonce))
      continue
    sentSignals.add(sig.nonce)
    if (sig.payload._toolbar) {
      handleToolbar(sig.payload._toolbar as Record<string, unknown>)
    }
    else if (sig.payload._action === 'increment_title') {
      state.titleCount++
      client.toolbar.set(c => ({ ...c, title: `${c.title?.replace(/\s*\d+$/, '') ?? ''} ${state.titleCount}` }))
    }
    else if (sig.payload._notify) {
      handleNotify(sig.payload._notify as { type: string, message: string })
    }
    else {
      client.signal.send(sig.payload as Signal)
    }
  }
}

// --- Service Call Bridge (Python → host AntConnect services) ---

interface ServiceRequest {
  id: string
  type?: string
  service: string
  method: string
  args: unknown[]
  url?: string
  data?: unknown
  params?: Record<string, string>
  headers?: Record<string, string>
}

const processedRequests = new Set<string>()

function handleServiceRequests(requests?: ServiceRequest[]) {
  if (!requests?.length || !client)
    return
  for (const req of requests) {
    if (processedRequests.has(req.id))
      continue
    processedRequests.add(req.id)
    const promise = req.type === 'http'
      ? client.request({ url: req.url!, method: req.method, data: req.data, params: req.params, headers: req.headers })
      : client.connect[req.service][req.method](...req.args)
    promise
      .then((data: unknown) => stSetValue({ type: 'response', id: req.id, data }))
      .catch((err: unknown) => stSetValue({ type: 'response', id: req.id, error: err instanceof Error ? err.message : String(err) }))
  }
}

// --- Toolbar & Notification Bridge (Python → host) ---

function handleToolbar(toolbar: Record<string, unknown>) {
  if (!client)
    return
  client.toolbar.set((current) => {
    const update = { ...current, ...toolbar } as typeof current
    const menu = toolbar.menu as Array<Record<string, string>> | undefined
    if (menu) {
      update.menu = menu.map((item) => {
        const onClick = item.action === 'increment_title'
          ? () => {
              state.titleCount++
              client!.toolbar.set(c => ({ ...c, title: `${c.title?.replace(/\s*\d+$/, '') ?? ''} ${state.titleCount}` }))
            }
          : item.notify
            ? () => client!.notifications[(item.notifyType ?? 'info') as 'info'](item.notify!)
            : undefined
        return { icon: item.icon, title: item.title, disabled: !!item.disabled, onClick }
      })
    }
    return update
  })
}

function handleNotify(n: { type: string, message: string }) {
  if (!client)
    return
  client.notifications[n.type as 'info'](n.message)
}

// --- ANT-Connect Bridge ---

let connectStarted = false

function connect() {
  if (connectStarted)
    return
  connectStarted = true

  if (!installRelay())
    return

  client = newCommsClient({ parent: window.parent })

  flushSignals()

  client.context
    .pipe(
      distinctUntilChanged((a, b) => JSON.stringify(a) === JSON.stringify(b)),
    )
    .subscribe(data => stSetValue({ type: 'context', data }))
}

// --- Bootstrap ---

window.addEventListener('message', (event) => {
  if (event.data?.type === 'streamlit:render') {
    connect()
    handleSignals(event.data.args?.signals)
    handleServiceRequests(event.data.args?.requests)
  }
  else if (event.data?.type === 'ant-deliver') {
    handleSignals(event.data.signals)
    handleServiceRequests(event.data.requests)
  }
})

stSetHeight(0)
stSetReady()
