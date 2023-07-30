from src.objects.api.input import *
from src.objects.api.output import *
from src.objects.api.session import FindingSession
from src.objects.rzd.suggests import Suggests
from src.processors.rzd.parsing import make_a_request
from src.queries.rzd.suggests import SuggestsRequest


class RequestHandler:
    def __init__(self, sessions: dict[str, FindingSession]) -> None:
        self.sessions = sessions
    
    def __call__(self, event: UserRequest) -> None:
        session = self.sessions.setdefault(
            event.author,
            FindingSession(),
        )
        
        if False:
            ...
        elif isinstance(event, SelectDepartureCity):
            resp = self.find_city_code(event.cityName)
        elif isinstance(event, SelectDestinationCity):
            resp = self.find_city_code(event.cityName)
        else:
            raise TypeError()

        session.history.append((event, resp))
    
    def find_city_code(
        self,
        cityName: str,
    ) -> CityHasBeenFound | CityHasNotBeenFound | TooManyCitiesHaveBeenFound:
        req = SuggestsRequest.model_validate(cityName)
        resp = make_a_request(req)
        if not isinstance(resp, Suggests): raise TypeError()
        
        if resp.city:
            if len(resp.city) == 1:
                if resp.city[0].expressCode:
                    return CityHasBeenFound(cityCode=resp.city[0].expressCode)
                else:
                    return CityHasNotBeenFound()
            else:
                return TooManyCitiesHaveBeenFound()
        else:
            return CityHasNotBeenFound()