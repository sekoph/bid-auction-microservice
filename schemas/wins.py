from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BaseWins(BaseModel):
    bid_id:int
    product_id:int

class CreateWins(BaseWins):
    pass

class Wins(BaseWins):
    id:int
    date_created: datetime
    class Config:
        from_attributes = True
