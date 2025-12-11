from pydantic import BaseModel


class GetWeatherResponse(BaseModel):
    city: str
    temp: float
