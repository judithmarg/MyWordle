from fastapi import APIRouter, Depends, HTTPException
from app.services import compare_word_data, verify_word_external
from app.schemas.game import WordPlayRequest, WordPlayUpdate, WordPlayResponse

router = APIRouter(prefix="wordle")

@router.post("/")
def compare_word_first(word_data: WordPlayRequest, db: Depends()):
    """
    Save the first attempt
    """
    response = create_wordle(word_data, db)
    if not response:
        raise HTTPException(status_code=404, detail="Error with save data wordle")
    return response

@router.put("/{play_id}")
def compare_word(play_id: int, word_data: WordPlayUpdate, db):
    """
    Compare with real word and changes the n tries 
    """
    response = update_wordle(play_id, word_data, db)
    if not response:
        raise HTTPException(status_code=404, detail="Error with save data wordle")
    return response


@router.get("/compare/{play_id}", response_model=WordPlayResponse)
def compare_word(play_id: int, db):
    """
    Compare the attempt with real_word
    """
    response = compare_word_data(play_id, db)
    if not response:
        raise HTTPException(status_code=404, detail="Error with wordle id, it might not exist ")
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
