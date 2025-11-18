from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Websockets demo</title>
        <!-- Bootstrap CSS (CDN) -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
    </head>
    <body class="bg-light">
      <div class="container py-5">
        <h1 class="mb-4">fasapi websocket api</h1>
        <h2 class="h4 mb-4">Your ClientID: <span id="ws-id"></span></h2>
        <div class="card">
          <div class="card-body">
            <h2 class="h5 mb-3">Input submit (click Send)</h2>
            <form id="demoForm" class="row g-3 align-items-end">
              <div class="col-md-8">
                <label for="textInput" class="form-label">Type something</label>
                <input type="text" class="form-control" id="textInput" name="text" placeholder="Type and click Send">
              </div>
              <div class="col-md-4 d-grid">
                <button type="button" id="sendBtn" class="btn btn-primary mt-4" disabled>Send</button>
              </div>
              <div class="col-12">
                <div class="mb-2"><strong>Submissions / Messages</strong></div>
                <ul id="resultsList" class="list-group"></ul>
              </div>
            </form>
          </div>
        </div>
      </div>

      <script>
        const input = document.getElementById('textInput');
        const sendBtn = document.getElementById('sendBtn');
        const resultsList = document.getElementById('resultsList');
        const wsIdSpan = document.getElementById('ws-id');

        function appendItem(text) {
          const li = document.createElement('li');
          li.className = 'list-group-item';
          li.textContent = text;
          resultsList.appendChild(li);
          li.scrollIntoView({ behavior: 'smooth', block: 'end' });
        }

        // create a client id and show it in the span
        const clientId = Date.now().toString(36) + Math.floor(Math.random()*10000).toString(36);
        wsIdSpan.textContent = clientId;

        // open websocket to server using correct protocol
        const protocol = location.protocol === 'https:' ? 'wss' : 'ws';
        const wsUrl = `${protocol}://${location.host}/ws/${encodeURIComponent(clientId)}`;
        let ws;

        function connectWebSocket() {
          ws = new WebSocket(wsUrl);

          ws.addEventListener('open', () => {
            appendItem('WebSocket connected');
            sendBtn.disabled = false;
          });

          ws.addEventListener('message', (event) => {
            // display incoming messages from server one-by-one
            appendItem(event.data);
          });

          ws.addEventListener('close', () => {
            appendItem('WebSocket disconnected');
            sendBtn.disabled = true;
            // optionally try to reconnect after a delay
            setTimeout(() => {
              appendItem('Reconnecting WebSocket...');
              connectWebSocket();
            }, 2000);
          });

          ws.addEventListener('error', (e) => {
            console.warn('WebSocket error', e);
          });
        }

        connectWebSocket();

        async function sendValue(value) {
          if (!value || !value.trim()) return;
          sendBtn.disabled = true;
          try {
            // prefer websocket if open
            if (ws && ws.readyState === WebSocket.OPEN) {
              ws.send(value);
              // also append immediately so user sees it (server may echo/broadcast separately)
              appendItem(`You: ${value}`);
            } else {
              // fallback to HTTP POST
              const resp = await fetch('/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: value })
              });
              if (!resp.ok) throw new Error('Network response was not ok');
              const data = await resp.json();
              appendItem(data.received ?? value);
            }
            input.value = '';
            input.focus();
          } catch (err) {
            appendItem('Error: ' + err.message);
          } finally {
            sendBtn.disabled = false;
          }
        }

        // send only on explicit Send button or Enter key — no automatic submit on change
        sendBtn.addEventListener('click', () => sendValue(input.value));

        input.addEventListener('keydown', (e) => {
          if (e.key === 'Enter') {
            e.preventDefault();
            sendValue(input.value);
          }
        });

        document.getElementById('demoForm').addEventListener('submit', (e) => e.preventDefault());
      </script>
    </body>
</html>
"""

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.post("/submit")
async def submit(request: Request):
    payload = await request.json()
    text = payload.get("text")
    return {"received": text}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} disconnected")
