from fastapi import FastAPI


app = FastAPI()


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
