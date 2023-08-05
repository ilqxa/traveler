from typing import ClassVar
from pydantic import BaseModel, ConfigDict, Field

from src.objects.rzd.prices import TrainPricing
from src.queries.rzd.common import CommonRequest


class TrainPricingQueryParams(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    serviceProvider: str = Field(alias='service_provider', default='B2B_RZD')


class TrainPricingRequestPayload(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    origin: str = Field(alias='Origin')
    destination: str = Field(alias='Destination')
    departureDate: str = Field(alias='DepartureDate')
    timeFrom: int = Field(alias='TimeFrom', default=0)
    timeTo: int = Field(alias='TimeTo', default=24)
    carGrouping: str = Field(alias='CarGrouping', default='DontGroup')
    getByLocalTime: bool = Field(alias='GetByLocalTime', default=True)
    specialPlacesDemand: str = Field(alias='SpecialPlacesDemand', default='StandardPlacesAndForDisabledPersons')


class TrainPricingRequest(CommonRequest):
    model_config = ConfigDict(frozen=True)
    
    url: str = Field(default='https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/TrainPricing', frozen=True)
    method: str = Field(default='POST', frozen=True)
    params: TrainPricingQueryParams = Field(default_factory=TrainPricingQueryParams)
    payload: TrainPricingRequestPayload = Field(alias='json')
    responseType: ClassVar = TrainPricing