from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas.bid_time import CreateBidTime, BidTimeSchema
from models.bid_time import BidTime


async def create_bid(db:Session, bid_time: CreateBidTime):
    try:
        new_bid_time = BidTime(**bid_time.model_dump())
        db.add(new_bid_time)
        db.commit()
        db.refresh(new_bid_time)
        return new_bid_time
    except IntegrityError:
        db.rollback()
        return False
    
    
    
async def get_bid_time_by_product(db:Session, product_id:int):
    return db.query(BidTime).filter(BidTime.product_id == product_id).first()


def get_bid_time(db: Session, skip:int, limit:int):
    return db.query(BidTime).offset(skip).limit(limit).all()