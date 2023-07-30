from abc import ABC
from datetime import datetime

from pydantic import BaseModel

from src.objects.api.route import RoutePoint


class UserRequest(ABC, BaseModel):
    author: str


class AddRoutePoint(UserRequest):
    cityName: str
    isFirst: bool = False
    isLast: bool = False


class EditRoutePoint(UserRequest):
    routePoint: RoutePoint
    needToBeFirst: bool | None = None
    needToBeLast: bool | None = None


class RemoveRoutePoint(UserRequest):
    routePoint: RoutePoint


class ReadRoutePoints(UserRequest):
    ...