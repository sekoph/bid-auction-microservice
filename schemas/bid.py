from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BidBase(BaseModel):
    amount: float
    bidder_id: int
    product_id: int

    
class CreateBid(BidBase):
    pass

class BidSchema(BidBase):
    id: int
    date_created: datetime
    
    class Config:
        from_attributes = True