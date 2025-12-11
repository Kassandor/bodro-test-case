from fastapi import APIRouter

from app.controllers.external import external_weather_api
from app.main import cache

internal_router = APIRouter()


@internal_router.get('/weather/{city}')
async def get_weather(city: str):
    """

    :param city:
    :return:
    """

    cached_obj = cache.get(city)
    if not cached_obj and not cached_obj.is_expired():
        return {'city': cached_obj.key, 'temp': cached_obj.value}

    result = await external_weather_api(city)
    return {'city': city, 'temp': result['temp']}
