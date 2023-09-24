import random
from bson import ObjectId
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import uvicorn
import json


class ServerData:
    def __init__(self, app, db_client):
        self.app = app
        self.db_client = db_client
        self.db_table = db_client["db"]["Articles"]
        self.articles = self.db_table.find()

    def refresh_articles(self):
        self.articles = self.db_table.find()

    @staticmethod
    def map_with_body(article: dict):
        a = {}
        a["title"] = article["title"]
        a["date"] = article["date"]
        a["tags"] = list(
            map(lambda x: x.strip(), article["hashtags"].strip().split(',')))
        a["id"] = str(article["_id"])
        a["images"] = article["urlToImage"]
        a["body"] = article["news_article"]
        test = (hash(article["title"])%40)*(hash(article["title"])/abs(hash(article["title"])))
        a["popularity"] = test
        return a

    @staticmethod
    def map_without_body(article: dict):
        a = server_data.map_with_body(article.copy())
        a['body'] = None
        return a


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

uri = "mongodb+srv://whyy:why_not@cluster0.m0qxirb.mongodb.net/?retryWrites=true&w=majority"
db_client = MongoClient(uri)

server_data = ServerData(app, db_client)

@server_data.app.get('/')
def root():
    return {'message': "Backend-Frontend Fetch Connection Successful"}


@server_data.app.get('/api/articles')
def list_articles(page: int = 1):
    random.seed(42)
    server_data.refresh_articles()
    # articles = server_data.articles[(page-1)*10: 10*page]
    cpy = list(server_data.articles).copy()
    articles = [cpy.pop(random.randint(0, len(cpy) - 1)) for _ in range(len(cpy))]
    articles = list(map(server_data.map_without_body, articles))
    return {"data": articles}


@server_data.app.get('/api/articles/{id}')
def show_article(id: str):
    random.seed(42)
    article = list(map(server_data.map_with_body,
                       server_data.db_table.find({"_id":ObjectId(id)})))
    return {"data": article}

@server_data.app.get('/api/ids')
def ids():
    document_ids = [str(document['_id']) for document in db_client["db"]["Articles"].find({}, projection={'_id': 1})]
    return {"data": document_ids}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
