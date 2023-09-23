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
        self.db_table = db_client["news"]["Articles"]
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
        a["id"] = article["_id"]
        a["images"] = article["urlToImage"]
        a["body"] = article["news_article"]
        a["popularity"] = (random.randint(-3000, 7000))/100
        return a

    @staticmethod
    def map_without_body(article: dict):
        a = article.copy()
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

uri = "mongodb+srv://muthu:adi123@cluster0.rgzozbh.mongodb.net/?retryWrites=true&w=majority"
db_client = MongoClient(uri)

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
    server_data.refresh_articles()
    articles = server_data.articles[(page-1)*10: 10*page]
    articles = list(map(server_data.map_without_body, articles))
    return json.dumps(articles)


@server_data.app.get('/api/articles/{id}')
def show_article(id: str):
    article = list(map(server_data.map_with_body,
                       server_data.db_table.find(ObjectId(id))))
    return json.dumps(article)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
