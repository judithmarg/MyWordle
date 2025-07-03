from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.game import delete_all_plays, get_all_wordle_plays, create_wordle, update_wordle, compare_word_data, verify_word_external
from app.schemas.game import WordPlayRequest, WordPlayUpdate, WordPlayResponse, WordCompareResponse
from app.database import get_db

router = APIRouter(prefix="/wordle")

@router.get("/")
def get_all_wordle_attempts(db: Session=Depends(get_db)):
    """
    Get all wordle played by users 
    """
    try:
        return get_all_wordle_plays(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=WordPlayResponse)
def create_word_first(word_data: WordPlayRequest, db: Session=Depends(get_db)):
    """
    Save the first attempt
    """
    try:
        response = create_wordle(word_data, db)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Error with save data wordle {e}")


@router.delete("/")
def delete_all(db: Session=Depends(get_db)):
    """
    Remove all wordle plays 
    """
    try:
        return delete_all_plays(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{play_id}", response_model=WordPlayResponse)
def update_word(play_id: int, word_data: WordPlayUpdate, db: Session=Depends(get_db)):
    """
    Change n tries automatically and update the new word
    """
    try:
        response = update_wordle(play_id, word_data, db)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/compare/{play_id}", response_model=WordCompareResponse)
def compare_word(play_id: int, db: Session=Depends(get_db)):
    """
    Compare the attempt with real_word
    """
    try:
        response = compare_word_data(play_id, db)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/verify/{word}")
def verify_word(word: str):
    """
    Verify the word with a dictionary
    """
    try:
        response = verify_word_external(word)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"Bad connection and {e}")
