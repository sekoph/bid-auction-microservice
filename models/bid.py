from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Float, func
from sqlalchemy.orm import relationship
from config.db import Base

class Bid(Base):
    __tablename__ = "user_bids"
    
    id = Column(Integer, primary_key=True, nullable= False)
    amount = Column(Float, nullable= False)
    bidder_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False, default=func.now())
    
    # relationship
    user_wins = relationship("Wins", back_populates="user_bids")