from pydantic import BaseModel, field_validator


class Station(BaseModel):
    NameRu: str | None
    NameEn: str | None
    StationName: str | None
    StationCode: str | None
    RegionName: str | None
    IsoCode: str | None
    ExpressCode: str | None
    CnsiCode: str | None