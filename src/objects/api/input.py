from abc import ABC
from datetime import datetime

from pydantic import BaseModel


class UserRequest(ABC, BaseModel):
    author: str


class SelectDepartureCity(UserRequest):
    cityName: str


class SelectDestinationCity(UserRequest):
    cityName: str