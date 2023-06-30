from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from blog.repository import user
from blog import schemas
from blog.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_by_id(id, db)
