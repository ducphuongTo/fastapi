from fastapi import FastAPI
from . import schemas, model
from .database import engine

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.post('/blog')
def createBlog(request: schemas.Blog):
    return request