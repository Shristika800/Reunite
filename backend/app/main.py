from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserResponse

app = FastAPI(title="Reunite API")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()