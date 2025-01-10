from fastapi import FastAPI, applications

from routes.bid import BidRouter
from routes.wins import winsRouter
from routes.bid_time import BidTimeRouter
from services.web_sockect import websocketRouter

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:8001',
    'http://localhost:8002',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(winsRouter)
app.include_router(BidTimeRouter)
app.include_router(BidRouter)
app.include_router(websocketRouter)



if __name__== "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=8003, reload=True)
    