from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
  
class WordPlayRequest(BaseModel):
    user_id: int
    to_compare_word: str
    word: str
    n_tries: int

class WordPlayUpdate(BaseModel):
    word: str

class WordPlayResponse(WordPlayRequest):
    id: int
    is_correct: bool
    time_now = datetime
    correct_pos_index = Optional(List[int]) = []
    different_pos_index = Optional(List[int]) = []
    incorrect_used_letters = Optional(List[str]) = []

