from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
  
class WordPlayRequest(BaseModel):
    user_id: int
    word_correct: str
    word_attempt: str
    n_tries: Optional[int] = 0

    class Config:
        from_attributes = True

class WordPlayUpdate(BaseModel):
    word: str

    class Config:
        from_attributes = True

class WordPlayResponse(WordPlayRequest):
    id: int
    is_correct: bool

    class Config:
        from_attributes = True
    
class WordIndex(BaseModel):
    word: str
    index: int

class WordCompareResponse(WordPlayResponse):
    correct_pos_index: Optional[List[WordIndex]] = []
    different_pos_index: Optional[List[WordIndex]] = []
    incorrect_used_letters: Optional[List[str]] = []

