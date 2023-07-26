from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config
from src.objects.rzd.stations import Station


class ActualMovement(BaseModel):
    model_config = model_config
    
    stationInfo: Station
    deviation: float
    deviationType: int