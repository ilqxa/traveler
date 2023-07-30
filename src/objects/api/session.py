from datetime import datetime

from pydantic import BaseModel, Field

from src.objects.api.input import *
from src.objects.api.output import *
from src.objects.api.route import RoutePoint


class FindingSession(BaseModel):
    history: list[tuple[UserRequest, UserResponse]] = []
    
    @property
    def actualRoutePoints(self) -> set[RoutePoint]:
        newRoutePoints = {
            resp.newRoutePoint for _, resp in self.history # type: ignore
            if isinstance(resp, (RoutePointHasBeenSet, RoutePointHasBeenUpdate))
        }
        oldRoutePoints = {
            resp.oldRoutePoint for _, resp in self.history # type: ignore
            if isinstance(resp, (RoutePointHasBeenUpdate, RoutePointHasBeenRemove))
        }
        
        return newRoutePoints.difference(oldRoutePoints)
    
    @property
    def firstPoint(self) -> RoutePoint | None:
        for rp in self.actualRoutePoints:
            if rp.isFirst:
                return rp
    
    @property
    def lastPoint(self) -> RoutePoint | None:
        for rp in self.actualRoutePoints:
            if rp.isLast:
                return rp