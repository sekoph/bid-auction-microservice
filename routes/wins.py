from sqlalchemy.orm import Session
from config.db import SessionLocal
from fastapi import APIRouter,Depends,HTTPException
from fastapi.background import BackgroundTasks
import time

from crud.wins import Get_Wins, Create_Wins,Get_Wins_By_Bid_Id
from schemas.wins import CreateWins,Wins


winsRouter = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
winsRouter.get('/api/wins' , response_model=list[Wins])
def get_wins(limit:int,skip:int,db:Session = Depends(get_db)):
    return Get_Wins(db=db,limit=limit,skip=skip)
    
    
winsRouter.post('/api/create_win' , response_model=Wins)
async def create_win(win:CreateWins,db:Session = Depends(get_db)):
    
    # highest_bid = db.query(Bid).filter(Bid.product_id == product_id).order_by(Bid.amount.desc()).first()
    
    new_win = Create_Wins(db=db,win=win)
    if new_win:
        return new_win
    else:
        raise HTTPException(status_code=400,detail="Bid not found")
    

winsRouter.get('/api/wins/{bid_id}' , response_model=Wins)
async def get_win_by_id(bid_id:int,db:Session = Depends(get_db)):
    return await Get_Wins_By_Bid_Id(db=db,bid_id=bid_id)