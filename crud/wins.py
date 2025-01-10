from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.wins import Wins
from schemas.wins import CreateWins

def Get_Wins(db:Session,limit:int,skip:int):
    return db.query(Wins).offset(skip).limit(limit).all()


async def Create_Wins(db:Session,bid_id:int,product_id:int):
    try:
        new_win = Wins(bid_id=bid_id,product_id=product_id)
        db.add(new_win)
        db.commit()
        db.refresh(new_win)
        return new_win
    except IntegrityError:
        db.rollback()
        return False
    
    
async def Get_Wins_By_Bid_Id(db:Session,bid_id:int):
    return db.query(Wins).filter(Wins.bid_id == bid_id).first()

async def Get_Wins_By_Product_Id(db:Session,product_id:int):
    return db.query(Wins).filter(Wins.product_id == product_id).first()
