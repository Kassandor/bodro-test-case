from pydantic.v1 import BaseModel


class GetWeatherRequest(BaseModel):
    city: str
