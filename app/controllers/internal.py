from fastapi import APIRouter

from cache.instances import cache
from controllers.external import external_weather_api
from dtos.requests import GetWeatherRequest
from dtos.responses import GetWeatherResponse


internal_router = APIRouter()


@internal_router.get('/weather/{city}')
async def get_weather(city: str) -> GetWeatherResponse:
    """
    Получение текущей погоды в городе
    :param city: Город
    :return: GetWeatherResponse
    """

    cached_obj = cache.get(city)
    if cached_obj and not cached_obj.is_expired():
        return GetWeatherResponse(city=cached_obj.key, temp=cached_obj.value)

    result: GetWeatherResponse = await external_weather_api(GetWeatherRequest(city=city))
    return result
