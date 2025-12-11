from fastapi import FastAPI

from cache.instances import InMemoryCacheDB
from controllers.external import external_router
from controllers.internal import internal_router

app = FastAPI()

app.include_router(external_router)
app.include_router(internal_router)
