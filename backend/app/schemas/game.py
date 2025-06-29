from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
  
class WordPlayRequest(BaseModel):
    user_id: int
    to_compare_word: str
    word: str
    n_tries: Optional[int] = 0

class WordPlayUpdate(BaseModel):
    word: str

class WordPlayResponse(WordPlayRequest):
    id: int
    created_at: datetime
    
class WordIndex(BaseModel):
    word: str
    index: int

class WordCompareResponse(WordPlayResponse):
    is_correct: bool
    correct_pos_index: Optional[List[WordIndex]] = []
    different_pos_index: Optional[List[WordIndex]] = []
    incorrect_used_letters: Optional[List[str]] = []

