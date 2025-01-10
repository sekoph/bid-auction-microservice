from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.bid import Bid
from schemas.bid import CreateBid, BidSchema
from datetime import time , timedelta,datetime


# function to create bid
from fastapi import HTTPException

async def Create_Bid(db: Session, bid: CreateBid) -> BidSchema:
    try:
        new_bid = Bid(**bid.model_dump())
        db.add(new_bid)
        db.commit()
        db.refresh(new_bid)
        return new_bid
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid bid data")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
def Get_Bid(db: Session, limit:int, skip: int):
    return db.query(Bid).offset(skip).limit(limit).all()


#get bid by id
def get_Bid_By_Id(db:Session, bid_id:int):
    return db.query(Bid).filter(Bid.id == bid_id).first()
        
        
def get_highset_bid(product_id: int, db: Session):
    return db.query(Bid).filter(Bid.product_id == product_id).order_by(Bid.amount.desc()).first()
    
    
def get_by_product_id(db: Session, product_id: int):
    return db.query(Bid).filter(Bid.product_id == product_id).first()