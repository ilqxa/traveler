from pydantic import BaseModel, Field

from src.queries.rzd.common import CommonRequest


class SuggestsQueryParams(BaseModel):
    query: str = Field(alias='Query')
    transportType: str = Field(alias='TransportType', default='bus,avia,rail,aeroexpress,suburban,boat')
    groupResults: bool = Field(alias='GroupResults', default=True)
    railwaySortPriority: bool = Field(alias='RailwaySortPriority', default=False)
    synonymOn: int = Field(alias='SynonymOn', default=1)


class SuggestsRequest(CommonRequest):
    url: str = Field(default='https://ticket.rzd.ru/api/v1/suggests')
    params: SuggestsQueryParams