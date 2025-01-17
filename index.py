from fastapi import FastAPI, applications
import asyncio
from routes.bid import BidRouter
from routes.wins import winsRouter
from routes.bid_time import BidTimeRouter
from services.web_sockect import websocketRouter

from fastapi.middleware.cors import CORSMiddleware

import py_eureka_client.eureka_client as eureka_client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

EUREKA_SERVER = os.getenv("EUREKA_SERVER")

# initialize Eureka client

async def register_with_eureka():
    await eureka_client.init_async(
        eureka_server=EUREKA_SERVER,
        app_name="auction-service",
        instance_host="localhost",
        instance_port=8003
    )
    
    
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(register_with_eureka())
# asyncio.run(register_with_eureka())

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
    