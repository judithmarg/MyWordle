from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(25), nullable=False) 
    email = Column(String(80), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    game_user_rel = relationship("Wordle", back_populates="play_rel")

