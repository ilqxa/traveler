from pydantic import BaseModel, Field

from src.queries.rzd.common import CommonRequest


class TrainPricingQueryParams(BaseModel):
    serviceProvider: str = Field(alias='service_provider', default='B2B_RZD')


class TrainPricingRequestPayload(BaseModel):
    origin: str = Field(alias='Origin')
    destination: str = Field(alias='Destination')
    departureDate: str = Field(alias='DepartureDate')
    timeFrom: int = Field(alias='TimeFrom', default=0)
    timeTo: int = Field(alias='TimeTo', default=24)
    carGrouping: str = Field(alias='CarGrouping', default='DontGroup')
    getByLocalTime: bool = Field(alias='GetByLocalTime', default=True)
    specialPlacesDemand: str = Field(alias='SpecialPlacesDemand', default='StandardPlacesAndForDisabledPersons')


class TrainPricingRequest(CommonRequest):
    url: str = Field(default='https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/TrainPricing')
    params: TrainPricingQueryParams
    json: TrainPricingRequestPayload