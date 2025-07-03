from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.wordle import Wordle
from app.schemas.game import WordPlayRequest, WordPlayUpdate, WordPlayResponse, WordCompareResponse

def get_all_wordle_plays(db: Session): 
    return db.query(Wordle).all()

def create_wordle(data: WordPlayRequest, db: Session):
    try:
        new_wordle = Wordle(
            user_id= data.user_id,
            word_correct= data.word_correct,
            word_attempt= data.word_attempt,
            n_tries= 1,
            is_correct= False,
        )
        db.add(new_wordle)
        db.commit()
        db.refresh(new_wordle)
        return new_wordle
    except Exception as e:
        raise ValueError(f"Error creating wordle game {e}")

def update_wordle(id: int, data: WordPlayUpdate, db: Session):
    wordle = db.query(Wordle).filter(Wordle.id == id).first()
    if not wordle:
        raise ValueError("Wordle not found with that id.")
   
    if wordle.n_tries == 5 :
        return wordle
    
    wordle.n_tries += 1
    wordle.word_attempt = data.word
    db.commit()
    db.refresh(wordle)

    return wordle

def delete_all_plays(db: Session):
    db_wordle = db.query(Wordle).all()
    for data in db_wordle:
        db.delete(data)
        db.commit()
    db.refresh()
    return { "message": "All of values were removed."}

def compare_word_data(id: int, db:Session):
    try:
        wordle = db.query(Wordle).filter(Wordle.id == id).first()
        if not wordle:
            raise ValueError("Wordle not found with that id.")
        
        word_attempt = wordle.word_attempt
        word_correct = wordle.word_correct
        correct = filter(lambda lind: lind[1] in word_correct and lind[1] == word_correct[lind[0]], enumerate(word_attempt))
        different = filter(lambda lind: lind[1] in word_correct and lind[1] != word_correct[lind[0]], enumerate(word_attempt))
        incorrect = [l for l in wordle.word_attempt if l not in word_correct ]

        return WordCompareResponse(
            user_id=wordle.user_id,
            word_correct=wordle.word_correct,
            word_attempt=wordle.word_attempt,
            n_tries=wordle.n_tries,
            id=wordle.id,
            is_correct=False,
            correct_pos_index=list(correct),
            different_pos_index=list(different),
            incorrect_used_letters=incorrect
        )
    
    except Exception as e:
        raise ValueError(f"Error comparing {e}")

def verify_word_external(word):
    return True