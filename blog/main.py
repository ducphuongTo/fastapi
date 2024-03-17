from fastapi import FastAPI
from . import schemas


app = FastAPI()

@app.post('/blog')
def createBlog(request: schemas.Blog):
    return request