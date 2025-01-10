from sqlalchemy.orm import Session
from config.db import SessionLocal
from fastapi import APIRouter, Depends , HTTPException, Body
from crud.bid_time import create_bid, get_bid_time, get_bid_time_by_product
from schemas.bid_time import CreateBidTime, BidTimeSchema
from datetime import datetime,time
from fastapi.background import BackgroundTasks
import time as time_module

from crud.bid import get_highset_bid
from crud.wins import Create_Wins

import requests
import asyncio




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

BidTimeRouter = APIRouter()

@BidTimeRouter.post('/api/bid/time', response_model = BidTimeSchema)
async def create_bid_time(product_id: int, hour:int,minute:int,second:int,background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    closing_time=time(hour,minute,second)
    
    bid_time = CreateBidTime(closing_time=closing_time, product_id=product_id)
    
    headers = {
    'Content-Type': 'application/json'
    }
    
    response = requests.put(f'http://localhost:8002/api/products/open/{product_id}', headers=headers)
    
    # print(response.json())

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Product not found")
    
    created = await create_bid(db, bid_time)
    
    bid = await get_bid_time_by_product(db, product_id)
    
    
    start_time = bid.start_time
    
    check = background_tasks.add_task( stop_bid, start_time, closing_time,product_id,db)
    if check:
        print("bid time created")
    else:
        print("bid time not created")
    
    # response1 = requests.put(f'http://localhost:8002/api/products/close/{product_id}',headers=headers)

    
    return created


"""function that ensure bidding is on during the time provided"""
async def stop_bid(start_time:time, closing_time:time, product_id:int,db):
    print(start_time)
    today = datetime.today()
    start_datetime = datetime.combine(today, start_time)
    closing_datetime = datetime.combine(today, closing_time)
    time_count = (closing_datetime - start_datetime).total_seconds()
    print("Task ongoing, will stop after:", time_count, "seconds")
    
    """"""
    # time_module.sleep(time_count)
    await asyncio.sleep(time_count)

    
    print("task completed")
    highest_bid = get_highset_bid(product_id, db)
    if highest_bid is None:
        print("No bids found for the product.")
        return None
    bid_id = highest_bid.id
    print("bid id", bid_id)
    await Create_Wins(db, bid_id,product_id)
    print("bid stopped and winner set")


@BidTimeRouter.get('/api/bid/time', response_model = list[BidTimeSchema])
def get_bid_time_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_bid_time(db, skip, limit)





# @BidTimeRouter.get('/api/bid/time/{product_id}', response_model = BidTimeSchema)
# def get_bid_time_by_product_id(product_id: int, db: Session = Depends(get_db)):
#     return get_bid_time_by_product(db, product_id)
    