from pydantic import BaseModel, field_validator

from src.rzd import model_config
from src.rzd.cars import Car
from src.rzd.stations import Station
from src.rzd.trains import Train, TrainPreview


class CarPricing(BaseModel):
    model_config = model_config
    
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
    
    originStationCode: str
    destinationStationCode: str
    trains: list[Train]
    clientFeeCalculation: bool
    agentFeeCalculation: bool
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
    moscowDateTime: str