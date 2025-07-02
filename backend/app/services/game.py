from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.wordle import Wordle
from app.schemas.game import WordPlayRequest, WordPlayUpdate, WordPlayResponse, WordCompareResponse

def get_all_wordle_plays(db: Session):
    t =  db.query(Wordle).all()
    return t

def create_wordle(data: WordPlayRequest, db: Session):
    try:
        new_wordle = Wordle(
            user_id= data.user_id,
            word_correct= data.word_correct,
            word_attempt= data.word_attempt,
            n_tries= 1,
            is_correct= False,
        )
        print(new_wordle)
        db.add(new_wordle)
        db.commit()
        db.refresh(new_wordle)
        return new_wordle
    except Exception as e:
        print(f"el error {e}")

def update_wordle(id: int, data: WordPlayUpdate, db: Session):
    wordle = db.query(Wordle).filter(Wordle.id == id).first()
    if not wordle:
        raise HTTPException(status_code=404, detail="Wordle not found with that id.")
   
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
            raise HTTPException(status_code=404, detail="Wordle not found with that id.")
        print(f"aca esta {wordle.id}")
        word_attempt = wordle.word_attempt
        word_correct = wordle.word_correct
        correct = filter(lambda l, ind: l in word_correct and l == word_correct[ind], word_attempt)
        different = filter(lambda l, ind: l in word_correct and l != word_correct[ind], word_attempt)
        incorrect = filter(lambda l: l not in word_correct, word_attempt)
        print(f"aqui los correctos: {correct}")
        return {
            "user_id":wordle.user_id,
            "word_correct":wordle.word_correct,
            "word_attempt":wordle.word_attempt,
            "n_tries":wordle.n_tries,
            "is_correct":len(incorrect) == 0 and len(different) == 0,
            "correct_pos_index":correct,
            "different_pos_index":different,
            "incorrect_used_letters":incorrect
        }
    except Exception as e:
        print(f"en este caso el error es {e}")

def verify_word_external(word):
    return True