from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from blog.hashing import Hash
from blog import schemas, models
from blog.database import get_db

router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=["User"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashedPassword = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/user/{id}", response_model=schemas.ShowUser, tags=["User"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found.")
    return user
