from typing import ClassVar
from pydantic import BaseModel, ConfigDict, Field

from src.objects.rzd.suggests import Suggests
from src.queries.rzd.common import CommonRequest


class SuggestsQueryParams(BaseModel):
    query: str = Field(alias='Query')
    transportType: str = Field(alias='TransportType', default='bus,avia,rail,aeroexpress,suburban,boat')
    groupResults: bool = Field(alias='GroupResults', default=True)
    railwaySortPriority: bool = Field(alias='RailwaySortPriority', default=False)
    synonymOn: int = Field(alias='SynonymOn', default=1)


class SuggestsRequest(CommonRequest):
    model_config = ConfigDict(frozen=True)
    
    url: str = Field(default='https://ticket.rzd.ru/api/v1/suggests', frozen=True)
    method: str = Field(default='GET', frozen=True)
    params: SuggestsQueryParams
    responseType: ClassVar = Suggests