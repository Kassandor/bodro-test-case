from fastapi import FastAPI

from app.cache.instances import InMemoryCacheDB

app = FastAPI()

cache = InMemoryCacheDB()


