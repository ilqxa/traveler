from pydantic import BaseModel, field_validator

from src.rzd import model_config


class Station(BaseModel):
    model_config = model_config
    
    nameRu: str | None
    nameEn: str | None
    stationName: str | None
    stationCode: str | None
    regionName: str | None
    isoCode: str | None
    expressCode: str | None
    cnsiCode: str | None