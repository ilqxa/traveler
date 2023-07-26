from pydantic import BaseModel, Field

from src.queries.rzd.common import CommonRequest


class CarPricingQueryParams(BaseModel):
    serviceProvider: str = Field(alias='service_provider', default='B2B_RZD')
    isBonusPurchase: bool = Field(default=False)


class CarPricingRequestPayload(BaseModel):
    originCode: str = Field(alias='OriginCode')
    destinationCode: str = Field(alias='DestinationCode')
    provider: str = Field(alias='Provider', default='P1')
    departureDate: str = Field(alias='DepartureDate')
    trainNumber: str = Field(alias='TrainNumber')
    onlyFpkBranded: bool = Field(alias='OnlyFpkBranded', default=False)
    specialPlacesDemand: str = Field(alias='SpecialPlacesDemand', default='StandardPlacesAndForDisabledPersons')


class CarPricingRequest(CommonRequest):
    url: str = Field(default='https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/CarPricing')
    params: CarPricingQueryParams
    json: CarPricingRequestPayload