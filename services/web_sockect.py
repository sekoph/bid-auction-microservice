from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.connection_manager import manager

websocketRouter = APIRouter()

@websocketRouter.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
