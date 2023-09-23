from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import uvicorn


class ServerData:
    def __init__(self, app, db):
        self.app = app
        self.db = db


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
db = redis.Redis(connection_pool=pool)

server_data = ServerData(app, db)


@server_data.on_event("startup")
async def startup_event():
    pass


@server_data.on_event("shutdown")
async def shutdown_event():
    pass


@server_data.app.get('/')
def root():
    return {'message': "Backend-Frontend Fetch Connection Successful"}


@server_data.app.get('/api/articles')
def articles(page: int = 1):
    return None


@server_data.app.get('/api/articles/{id}')
def articles(id: int):
    return None


@server_data.app.get('/api/search')
def articles(q: str):
    return None


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
