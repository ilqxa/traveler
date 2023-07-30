from src.objects.api.input import *
from src.objects.api.output import *
from src.objects.api.session import FindingSession
from src.objects.rzd.suggests import Suggests
from src.processors.rzd.parsing import make_a_request
from src.queries.rzd.suggests import SuggestsRequest


class RequestHandler:
    def __init__(self, sessions: dict[str, FindingSession]) -> None:
        self.sessions = sessions
    
    def __call__(self, event: UserRequest) -> UserResponse:
        session = self.sessions.setdefault(
            event.author,
            FindingSession(),
        )
        
        if False:
            ...
        
        elif isinstance(event, AddRoutePoint):
            resp = self._add_route_point(
                cityName = event.cityName,
                needToBeFirst = event.isFirst,
                needToBeLast = event.isLast,
            )
            
            if event.isFirst and (oldFirstPoint := session.firstPoint):
                correct = self._edit_route_point(oldFirstPoint, needToBeFirst=False)
                if isinstance(correct, RoutePointHasNothingToUpdate): raise Exception()
                session.history.append((event, correct))
                
            if event.isLast and (oldLastPoint := session.lastPoint):
                correct = self._edit_route_point(oldLastPoint, needToBeLast=False)
                if isinstance(correct, RoutePointHasNothingToUpdate): raise Exception()
                session.history.append((event, correct))
            
        elif isinstance(event, EditRoutePoint):
            resp = self._edit_route_point(
                oldRoutePoint = event.routePoint,
                needToBeFirst = event.needToBeFirst,
                needToBeLast = event.needToBeLast,
            )
            
            if event.needToBeFirst and (oldFirstPoint := session.firstPoint):
                correct = self._edit_route_point(oldFirstPoint, needToBeFirst=False)
                if isinstance(correct, RoutePointHasNothingToUpdate): raise Exception()
                session.history.append((event, correct))
                
            if event.needToBeLast and (oldLastPoint := session.lastPoint):
                correct = self._edit_route_point(oldLastPoint, needToBeLast=False)
                if isinstance(correct, RoutePointHasNothingToUpdate): raise Exception()
                session.history.append((event, correct))
            
        elif isinstance(event, RemoveRoutePoint):
            resp = RoutePointHasBeenRemove(
                oldRoutePoint = event.routePoint,
            )
        
        elif isinstance(event, ReadRoutePoints):
            resp = RoutePointsList(
                routePoints = list(session.actualRoutePoints),
            )
        
        else:
            raise TypeError()

        session.history.append((event, resp))
        return resp
    
    def _add_route_point(
        self,
        cityName: str,
        needToBeFirst: bool,
        needToBeLast: bool,
    ) -> RoutePointHasBeenSet | CityHasNotBeenFound | TooManyCitiesHaveBeenFound:
        req = SuggestsRequest.model_validate(cityName)
        resp = make_a_request(req)
        if not isinstance(resp, Suggests): raise TypeError()
        
        if resp.city:
            if len(resp.city) == 1:
                if resp.city[0].expressCode:
                    rp = RoutePoint(
                        cityCode = resp.city[0].expressCode,
                        isFirst = needToBeFirst,
                        isLast = needToBeLast,
                    )
                    return RoutePointHasBeenSet(newRoutePoint=rp)
                else:
                    return CityHasNotBeenFound()
            else:
                return TooManyCitiesHaveBeenFound()
        else:
            return CityHasNotBeenFound()
    
    def _edit_route_point(
        self,
        oldRoutePoint: RoutePoint,
        needToBeFirst: bool | None = None,
        needToBeLast: bool | None = None,
    ) -> RoutePointHasBeenUpdate | RoutePointHasNothingToUpdate:
        if (
            (needToBeFirst is not None and needToBeFirst != oldRoutePoint.isFirst) or
            (needToBeLast is not None and needToBeLast != oldRoutePoint.isLast)
        ):
            newRoutePoint = RoutePoint(
                cityCode = oldRoutePoint.cityCode,
                isFirst = needToBeFirst if needToBeFirst is not None else oldRoutePoint.isFirst,
                isLast = needToBeLast if needToBeLast is not None else oldRoutePoint.isLast,
            )
            return RoutePointHasBeenUpdate(
                oldRoutePoint = oldRoutePoint,
                newRoutePoint = newRoutePoint,
            )
        else:
            return RoutePointHasNothingToUpdate(routePoint=oldRoutePoint)