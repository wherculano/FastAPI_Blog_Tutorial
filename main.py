from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"data":"Hello World!"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": f"comments from ID {id}"}


