from fastapi import FastAPI
from typing import Optional

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

# @app.get('/blog/{id}')
# def show(id: int):
#     return {'data': id}


# @app.get('/blog/{id}/comments')
# def show(id: int):
#     return {'data': 'comments'}

