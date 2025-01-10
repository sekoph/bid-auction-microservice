from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Float, func, select,Time
from sqlalchemy.orm import relationship
from config.db import Base

class BidTime(Base):
    __tablename__ = 'user_bid_time'
    
    id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, index=True, nullable=False, unique=True)
    date_created = Column(DateTime, default=func.now(), nullable=False)
    start_time = Column(Time, default=func.current_time(), nullable=False)
    closing_time = Column(Time, index=True, nullable=False)
    
