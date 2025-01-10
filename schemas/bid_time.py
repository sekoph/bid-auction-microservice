from pydantic import BaseModel
from datetime import datetime,time
from typing import Optional


class BidTimeBase(BaseModel):
    closing_time: time
    product_id: int

class CreateBidTime(BidTimeBase):
    pass


class BidTimeSchema(BidTimeBase):
    id: int
    date_created:datetime
    start_time: time
    
    class config:
        from_attributes = True
