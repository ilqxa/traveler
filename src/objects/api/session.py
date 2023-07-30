from datetime import datetime

from pydantic import BaseModel, Field

from src.objects.api.input import *
from src.objects.api.output import *


class FindingSession(BaseModel):
    history: list[tuple[UserRequest, UserResponse]] = []
    
    @property
    def _departureCode(self) -> str | None:
        for req, resp in self.history[::-1]:
            if isinstance(req, SelectDepartureCity) and isinstance(resp, CityHasBeenFound):
                return resp.cityCode
    
    @property
    def _destinationCode(self) -> str | None:
        for req, resp in self.history[::-1]:
            if isinstance(req, SelectDestinationCity) and isinstance(resp, CityHasBeenFound):
                return resp.cityCode