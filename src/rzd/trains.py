from pydantic import BaseModel, field_validator

from src.rzd.cars import CarGroup
from src.rzd.movement import ActualMovement
from src.rzd.stations import Station


class TrainPreview(BaseModel):
    TrainNumber: str
    TrainNumberToGetRoute: str
    DisplayTrainNumber: str
    TrainDescription: str
    TrainName: str
    TrainNameEn: str
    TransportType: str
    OriginName: str
    InitialStationName: str
    OriginStationCode: str
    OriginStationInfo: Station
    InitialTrainStationCode: str
    InitialTrainStationCnsiCode: str
    DestinationName: str
    FinalStationName: str
    DestinationStationCode: str
    DestinationStationInfo: Station
    FinalTrainStationCode: str
    FinalTrainStationCnsiCode: str
    DestinationNames: list[str]
    FinalStationNames: list[str]
    DepartureDateTime: str
    LocalDepartureDateTime: str
    ArrivalDateTime: str
    LocalArrivalDateTime: str
    ArrivalDateTimes: list[str]
    LocalArrivalDateTimes: list[str]
    DepartureDateFromFormingStation: str
    DepartureStopTime: int
    ArrivalStopTime: int
    TripDuration: float
    TripDistance: int
    IsSuburban: bool
    IsComponent: bool
    CarServices: list
    IsSaleForbidden: bool
    IsTicketPrintRequiredForBoarding: bool
    BookingSystem: str
    IsVrStorageSystem: bool
    PlacesStorageType: str
    BoardingSystemTypes: list[str]
    TrainBrandCode: str


class Train(TrainPreview):
    CarGroups: list[CarGroup]
    IsFromSchedule: bool
    IsTourPackagePossible: bool
    CarTransportationsFreePlacesCount: None
    ActualMovement: ActualMovement
    CategoryId: None
    ScheduleId: None
    Provider: str
    HasElectronicRegistration: bool
    HasCarTransportationCoaches: bool
    HasDynamicPricingCars: bool
    HasTwoStoreyCars: bool
    HasSpecialSaleMode: bool
    Carriers: list[str]
    CarrierDisplayNames: list[str]
    Id: int
    IsBranded: bool
    DestinationStationName: str
    OriginStationName: str