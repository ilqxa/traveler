from typing import ClassVar
from pydantic import BaseModel, ConfigDict, Field

from src.objects.rzd.prices import CarPricing
from src.queries.rzd.common import CommonRequest


class CarPricingQueryParams(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    serviceProvider: str = Field(alias='service_provider', default='B2B_RZD')
    isBonusPurchase: bool = Field(default=False)


class CarPricingRequestPayload(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    originCode: str = Field(alias='OriginCode')
    destinationCode: str = Field(alias='DestinationCode')
    provider: str = Field(alias='Provider', default='P1')
    departureDate: str = Field(alias='DepartureDate')
    trainNumber: str = Field(alias='TrainNumber')
    onlyFpkBranded: bool = Field(alias='OnlyFpkBranded', default=False)
    specialPlacesDemand: str = Field(alias='SpecialPlacesDemand', default='StandardPlacesAndForDisabledPersons')


class CarPricingRequest(CommonRequest):
    model_config = ConfigDict(frozen=True)
    
    url: str = Field(default='https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/CarPricing', frozen=True)
    method: str = Field(default='POST', frozen=True)
    params: CarPricingQueryParams = Field(default_factory=CarPricingQueryParams)
    payload: CarPricingRequestPayload = Field(alias='json')
    responseType: ClassVar = CarPricing