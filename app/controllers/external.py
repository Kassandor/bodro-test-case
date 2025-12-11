import asyncio
import random
from time import monotonic

from fastapi import APIRouter

from app.cache.instances import CachedObject
from app.main import cache

external_router = APIRouter()

RATE_LIMIT = 5
CAPACITY_LIMIT = 5
tokens = CAPACITY_LIMIT
last_refill = monotonic()


@external_router.get("/api/external_weather/{city}")
async def external_weather_api(city: str) -> dict:
    """
    :param city:
    :return:
    """
    await asyncio.sleep(0.1)  # имитация сетевой задержки
    temp = random.randint(10, 30)
    cached_obj = CachedObject(city, temp)
    cache.put(cached_obj)
    return {'city': city, 'temp': cached_obj.value}
