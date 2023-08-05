from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config


class Station(BaseModel):
    model_config = model_config
    
    nameRu: str | None = None
    nameEn: str | None = None
    stationName: str | None
    stationCode: str | None
    regionName: str | None
    isoCode: str | None
    expressCode: str | None = None
    cnsiCode: str | None