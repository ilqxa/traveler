from pydantic import BaseModel, field_validator

from src.objects.rzd import split_numbers_list, model_config


class Point(BaseModel):
    model_config = model_config
    
    nodeId: str
    expressCode: str
    name: str
    nodeType: str
    transportType: str
    region: str
    regionIso: str
    countryIso: str
    aviaCode: str | None = None
    busCode: str | None = None
    suburbanCode: list[str]
    foreignCode: str
    expressCodes: list[str] | None = None
    hasAeroExpress: bool
    
    split_codes = field_validator('suburbanCode', 'expressCodes', mode='before')(split_numbers_list)


class Suggests(BaseModel):
    model_config = model_config
    
    city: list[Point]
    train: list[Point]
    avia: list[Point]