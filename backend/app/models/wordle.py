from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Wordle(Base):
    __tablename__ = "wordle_data"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    word_correct = Column(String(5), nullable=False)
    n_tries = Column(Integer, default=0 ,nullable=False)
    is_correct = Column(Boolean, default=False )

    play_rel = relationship("User", back_populates="game_user_rel")