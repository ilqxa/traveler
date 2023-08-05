from pydantic import BaseModel, field_validator

from src.objects.rzd import split_numbers_list, model_config


class Point(BaseModel):
    nodeId: str
    expressCode: str | None = None
    name: str
    nodeType: str
    transportType: str
    region: str
    regionIso: str
    countryIso: str
    aviaCode: str | None = None
    busCode: str | None = None
    suburbanCode: list[str] | None = None
    foreignCode: str | None = None
    expressCodes: list[str] | None = None
    hasAeroExpress: bool
    
    split_codes = field_validator('suburbanCode', 'expressCodes', mode='before')(split_numbers_list)


class Suggests(BaseModel):    
    city: list[Point] | None = None
    train: list[Point] | None = None
    avia: list[Point] | None = None