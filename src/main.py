from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import uvicorn
import json


class ServerData:
    def __init__(self, app, db_client):
        self.app = app
        self.db_client = db_client


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

db_client = redis.Redis(host='localhost', port=6379, db=0)

server_data = ServerData(app, db_client)


@server_data.on_event("startup")
def startup_event():
    pass


@server_data.on_event("shutdown")
def shutdown_event():
    pass


@server_data.app.get('/')
def root():
    return {'message': "Backend-Frontend Fetch Connection Successful"}


@server_data.app.get('/api/articles')
def list_articles(page: int = 1):
    articles = [{} for _ in range(10)]
    return json.dumps(articles)


@server_data.app.get('/api/articles/{id}')
def show_article(id: int):
    article = server_data.db_client.get(id)
    return json.dumps(article)


@server_data.app.get('/api/search')
def search_articles(q: str):
    articles = []
    return json.dumps(articles)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
