from pydantic import BaseModel, field_validator

from src.rzd.stations import Station


class ActualMovement(BaseModel):
    StationInfo: Station
    Deviation: float
    DeviationType: int