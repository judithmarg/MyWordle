from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.wordle import Wordle
from app.schemas.game import WordPlayRequest, WordPlayUpdate, WordPlayResponse, WordCompareResponse

def get_all_wordle_plays(db: Session):
    return db.query(Wordle).all()

def create_wordle(data: WordPlayRequest, db: Session):
    new_wordle = Wordle(
        user_id= data.user_id,
        word_correct= data.to_compare_word,
        word_attempt= data.word,
        n_tries= 1,
    )
    db.add(new_wordle)
    db.commit()
    db.refresh(new_wordle)
    return new_wordle

def update_wordle(id: int, data: WordPlayUpdate, db: Session):
    wordle = db.query(Wordle).filter(Wordle.id == id).first()
    if not wordle:
        raise HTTPException(status_code=404, detail="Wordle not found with that id.")
   
    if wordle["n_tries"] == 5 :
        return wordle
    
    wordle["n_tries"] += 1
    wordle["word_attempt"] = data.word
    db.commit()
    db.refresh(wordle)
    return wordle

def compare_word_data(id: int, db:Session):
    wordle = db.query(Wordle).filter(Wordle.id == id).first()
    if not wordle:
        raise HTTPException(status_code=404, detail="Wordle not found with that id.")
    
    word_attempt = wordle["word_attempt"]
    word_correct = wordle["word_correct"]
    correct = filter(lambda l, ind: l in word_correct and l == word_correct[ind], word_attempt)
    different = filter(lambda l, ind: l in word_correct and l != word_correct[ind], word_attempt)
    incorrect = filter(lambda l: l not in word_correct, word_attempt)
    print(f"aqui los correctos: {correct}")


    return True

def verify_word_external(word):
    return True