from typing import Literal
from pydantic import BaseModel, ConfigDict


class TrainPlace(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    trainNumber: str
    carNumber: str
    compartmentNumber: str
    placeNumber: str
    carType: Literal['КУПЕ', 'ПЛАЦ']
    price: float
    isLower: bool
    isSide: bool
    isNearToilet: bool