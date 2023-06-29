from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get("/")
def index() -> dict[str, str]:
    return {"data": "Hello World!"}


@app.get("/blog/unpublished")
def unpublished() -> dict[str, str]:
    return {"data": "unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int) -> dict[str, str]:
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int) -> dict[str, str]:
    return {"data": f"comments from ID {id}"}


@app.get("/blog")
def blog(limit: int = 10, published: bool = False) -> dict[str, str]:
    if published:
        return {"data": f"{limit} published blogs from the db"}
    return {"data": f"{limit} blogs from the db"}


@app.post("/blog")
def create_blog(blog: Blog) -> dict[str, str]:
    return {"data": f"Blog is created with title as '{blog.title}'"}
