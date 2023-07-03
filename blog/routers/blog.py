from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from blog import schemas, oauth2
from blog.database import get_db
from blog.repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request, current_user)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get("/{id}", response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.select_by_id(id, db)
