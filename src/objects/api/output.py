from abc import ABC
from datetime import datetime

from pydantic import BaseModel

from src.objects.api.route import RoutePoint


class UserResponse(ABC, BaseModel):
    text: str


class CityHasNotBeenFound(UserResponse):
    text: str = ''


class TooManyCitiesHaveBeenFound(UserResponse):
    text: str = ''


class RoutePointHasBeenSet(UserResponse):
    text: str = ''
    newRoutePoint: RoutePoint


class RoutePointHasBeenUpdate(UserResponse):
    text: str = ''
    oldRoutePoint: RoutePoint
    newRoutePoint: RoutePoint


class RoutePointHasNothingToUpdate(UserResponse):
    text: str = ''
    routePoint: RoutePoint


class RoutePointDoesNotExist(UserResponse):
    text: str = ''
    routePoint: RoutePoint


class RoutePointHasBeenRemove(UserResponse):
    text: str = ''
    oldRoutePoint: RoutePoint


class RoutePointsList(UserResponse):
    text: str = ''
    routePoints: list[RoutePoint]