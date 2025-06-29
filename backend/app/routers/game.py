from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.game import get_all_wordle_plays, create_wordle, update_wordle, compare_word_data, verify_word_external
from app.schemas.game import WordPlayRequest, WordPlayUpdate, WordPlayResponse, WordCompareResponse
from app.database import get_db

router = APIRouter(prefix="/wordle")

@router.post("/", response_model=WordPlayResponse)
def compare_word_first(word_data: WordPlayRequest, db: Session=Depends(get_db)):
    """
    Save the first attempt
    """
    response = create_wordle(word_data, db)
    if not response:
        raise HTTPException(status_code=404, detail="Error with save data wordle")
    return response

@router.put("/{play_id}", response_model=WordPlayResponse)
def compare_word(play_id: int, word_data: WordPlayUpdate, db: Session=Depends(get_db)):
    """
    Change n tries automatically and update the new word
    """
    response = update_wordle(play_id, word_data, db)
    if not response:
        raise HTTPException(status_code=404, detail="Error with save data wordle")
    return response

@router.get("/", response_model=List[WordPlayResponse])
def get_all_wordle_attempts(db: Session=Depends(get_db)):
    """
    Get all wordle played by users 
    """
    return get_all_wordle_plays(db)

@router.get("/compare/{play_id}", response_model=WordCompareResponse)
def compare_word(play_id: int, db: Session=Depends(get_db)):
    """
    Compare the attempt with real_word
    """
    response = compare_word_data(play_id, db=Depends(get_db))
    if not response:
        raise HTTPException(status_code=404, detail="Error with wordle id, it might not exist.")
    return response

@router.get("/verify/{word}")
def verify_word(word: str):
    """
    Verify the word with a dictionary
    """
    response = verify_word_external(word)
    if not response:
        raise HTTPException(status_code=404, detail="Bad connection with third app service")
    return response
