from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    db.commit()
    return f"Blog with id {id} was deleted."


@app.get("/blog", status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}")
def show(id: int, response: Response, db: Session = Depends(get_db),):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": f"Blog with id {id} is not available."}
    return blogs
