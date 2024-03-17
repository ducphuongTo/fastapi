from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

app = FastAPI()

@app.get("/blog")
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog list from db'}
    else:
        return {'data': f'{limit} published blog list'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all published blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def show(id: int, limit = 10):
    return {'data': 'comments'}

@app.post('/blog/')
def createBlog(request: Blog):
   return {'data': f"Blog is created with title {request.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)