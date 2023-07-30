from abc import ABC
from datetime import datetime

from pydantic import BaseModel


class UserResponse(ABC, BaseModel):
    text: str


class CityHasBeenFound(UserResponse):
    text: str = ''
    cityCode: str


class CityHasNotBeenFound(UserResponse):
    text: str = ''


class TooManyCitiesHaveBeenFound(UserResponse):
    text: str = ''