from datetime import datetime
from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config
from src.objects.rzd.cars import Car
from src.objects.rzd.stations import Station
from src.objects.rzd.trains import Train, TrainPreview


class CarPricing(BaseModel):
    model_config = model_config
    
    def __hash__(self) -> int:
        return hash(self.model_dump_json())
    
    originCode: str
    destinationCode: str
    originTimeZoneDifference: int
    destinationTimeZoneDifference: int
    cars: list[Car]
    routePolicy: str
    trainInfo: TrainPreview
    allowedDocumentTypes: list[str]
    clientFeeCalculation: None
    agentFeeCalculation: None
    bookingSystem: str
    carTariffPrices: None


class TrainPricing(BaseModel):
    model_config = model_config
    
    def __hash__(self) -> int:
        return hash(self.model_dump_json())
    
    originStationCode: str
    destinationStationCode: str
    trains: list[Train]
    clientFeeCalculation: bool | None
    agentFeeCalculation: bool | None
    originCode: str
    originStationInfo: Station
    originTimeZoneDifference: int
    destinationCode: str
    destinationStationInfo: Station
    destinationTimeZoneDifference: int
    routePolicy: str
    departureTimeDescription: str
    arrivalTimeDescription: str
    notAllTrainsReturned: bool
    stationClarifying: None
    bookingSystem: str
    id: int
    destinationStationName: str
    originStationName: str
    moscowDateTime: datetime