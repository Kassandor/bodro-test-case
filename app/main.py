from fastapi import FastAPI

from app.cache.instances import InMemoryCacheDB
from app.controllers.external import external_router
from app.controllers.internal import internal_router

app = FastAPI()
cache = InMemoryCacheDB()

app.include_router(external_router)
app.include_router(internal_router)
