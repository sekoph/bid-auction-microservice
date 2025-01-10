from config.db import Base
from sqlalchemy import Integer,Column,ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

class Wins(Base):
    __tablename__ = "user_wins"
    
    id = Column(Integer,primary_key=True,nullable=False)
    bid_id = Column(Integer, ForeignKey("user_bids.id"),nullable=False, unique=True)
    date_created = Column(DateTime, default=func.now(), nullable=False)
    product_id = Column(Integer, index=True, nullable=False, unique=True)
    
    user_bids = relationship("Bid", back_populates="user_wins")