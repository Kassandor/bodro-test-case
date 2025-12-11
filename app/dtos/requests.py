from pydantic import BaseModel


class GetWeatherRequest(BaseModel):
    city: str
