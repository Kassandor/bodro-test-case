import asyncio
import random
from time import monotonic

from fastapi import APIRouter, HTTPException

from cache.instances import CachedObject, cache
from dtos.requests import GetWeatherRequest
from dtos.responses import GetWeatherResponse

external_router = APIRouter()

# Количество токенов
CAPACITY = 5
tokens = CAPACITY

# Текущее время со старта системы
last_window = int(monotonic())
# Защита от гонок
_lock = asyncio.Lock()


async def take_token():
    """
    Получение токена для вызова внешнего апи
    """
    global tokens, last_window

    async with _lock:
        current_window = int(monotonic())

        # Если прошла секунда - доступно CAPACITY запросов
        if current_window != last_window:
            last_window = current_window
            tokens = CAPACITY

        # Если есть токены - продолжаем вызова внешнего апи
        if tokens > 0:
            tokens -= 1
            return

        # Если токены кончились - 429
        raise HTTPException(status_code=429, detail='Максимум 5 запросов в сек')


@external_router.get("/api/external_weather/{city}")
async def external_weather_api(body: GetWeatherRequest) -> GetWeatherResponse:
    """
    Получение данных с внешнего апи
    :param body: GetWeatherRequest
    :return: GetWeatherResponse
    """
    await take_token()

    await asyncio.sleep(0.1)  # имитация сетевой задержки
    temp = random.randint(10, 30)
    cached_obj = CachedObject(body.city, temp)
    cache.put(cached_obj)
    return GetWeatherResponse(city=body.city, temp=temp)
