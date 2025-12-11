from fastapi import APIRouter

from app.controllers.external import external_weather_api
from app.dtos.requests import GetWeatherRequest
from app.dtos.responses import GetWeatherResponse
from app.main import cache

internal_router = APIRouter()


@internal_router.get('/weather/{city}')
async def get_weather(body: GetWeatherRequest) -> GetWeatherResponse:
    """
    Получение текущей погоды в городе
    :param body: GetWeatherRequest
    :return:
    """

    cached_obj = cache.get(body.city)
    if cached_obj and not cached_obj.is_expired():
        return GetWeatherResponse(city=cached_obj.key, temp=cached_obj.value)

    result = await external_weather_api(body)
    return GetWeatherResponse(city=body.city, temp=result['temp'])
