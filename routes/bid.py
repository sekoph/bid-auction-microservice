from sqlalchemy.orm import Session
from config.db import SessionLocal
from fastapi import APIRouter, Depends , HTTPException, Body, WebSocket, WebSocketDisconnect

from crud.bid import Create_Bid, Get_Bid, get_Bid_By_Id, get_by_product_id
from schemas.bid import CreateBid,BidSchema
from crud.wins import Get_Wins_By_Product_Id

from services.kafkaConfig.producer import send_to_kafka
from services.kafkaConfig.consumer import start_kafka_consumer
from services.requests import fetch_data
import asyncio
import random



from typing import Annotated


# define dependancy

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# define the routers

BidRouter = APIRouter()

@BidRouter.on_event("startup")
async def startup_event():
    asyncio.create_task(start_kafka_consumer())

@BidRouter.post('/api/bid/add', response_model = BidSchema)
async def create_bid(token: str, product_id: int,amount: float , db: Session = Depends(get_db)):
    
    headers = {
    'Authorization': 'Bearer '+ token,
    'Content-Type': 'application/json'
    }
    
    headers2 = {
    'Content-Type': 'application/json'
    }
    
    # product = await fetch_data(f'http://localhost:8002/api/products/{product_id}', headers=headers2)
    # product_response = requests.get(f'http://localhost:8002/api/products/{product_id}', headers=headers2)
    
    product = await fetch_data(f'api/products/{product_id}', service_name="product-service", method='get', headers=headers2)
    bidder = await fetch_data(f'api/user/me',service_name="user-service", method='get', headers=headers)


    # bidder = random.randint(1,10)

    
    print(product)
    product_price = product['disposal_price']
    
    if amount < product_price:
        raise HTTPException(status_code=400, detail="Bid amount must be greater than or equal to the product price.")
    new_bid = CreateBid(amount=amount, bidder_id=bidder['id'], product_id=product_id)
    
    # sending kafka message
    
    data_to_kafka = {"bidder_id": bidder, "product_id": product_id, "amount": amount}
    
    # await send_to_kafka(data_to_kafka)
    send = asyncio.create_task(send_to_kafka(data_to_kafka))
    if not send:
        raise HTTPException(status_code=400, detail="Failed to send message to Kafka.")
    
    return await Create_Bid(db,new_bid)

# to run kafka consumer backgound



@BidRouter.get('/api/bid', response_model = list[BidSchema])
def get_bids(limit: int = 100, skip:int = 0, db: Session = Depends(get_db)):
    return Get_Bid(db = db, limit = limit, skip = skip)


@BidRouter.get('/api/bid/{bid_id}', response_model=BidSchema)
def get_bid_by_id(bid_id:int, db:Session = Depends(get_db)):
    return get_Bid_By_Id(db, bid_id)


@BidRouter.get('/api/bid/product/{product_id}')
async def get_won_product(product_id:int,db:Session = Depends(get_db)):
    product = await Get_Wins_By_Product_Id(db, product_id)
    print(product)
    return product