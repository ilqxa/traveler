from pydantic import BaseModel, field_validator

from src.rzd.cars import Car
from src.rzd.stations import Station
from src.rzd.trains import Train, TrainPreview


class CarPricing(BaseModel):
    OriginCode: str
    DestinationCode: str
    OriginTimeZoneDifference: int
    DestinationTimeZoneDifference: int
    Cars: list[Car]
    RoutePolicy: str
    TrainInfo: TrainPreview
    AllowedDocumentTypes: list[str]
    ClientFeeCalculation: None
    AgentFeeCalculation: None
    BookingSystem: str
    CarTariffPrices: None


class TrainPricing(BaseModel):
    OriginStationCode: str
    DestinationStationCode: str
    Trains: list[Train]
    ClientFeeCalculation: bool
    AgentFeeCalculation: bool
    OriginCode: str
    OriginStationInfo: Station
    OriginTimeZoneDifference: int
    DestinationCode: str
    DestinationStationInfo: Station
    DestinationTimeZoneDifference: int
    RoutePolicy: str
    DepartureTimeDescription: str
    ArrivalTimeDescription: str
    NotAllTrainsReturned: bool
    StationClarifying: None
    BookingSystem: str
    Id: int
    DestinationStationName: str
    OriginStationName: str
    MoscowDateTime: str