from pydantic import BaseModel, field_validator

from src.rzd import model_config
from src.rzd.cars import CarGroup
from src.rzd.movement import ActualMovement
from src.rzd.stations import Station


class TrainPreview(BaseModel):
    model_config = model_config
    
    trainNumber: str
    trainNumberToGetRoute: str
    displayTrainNumber: str
    trainDescription: str
    trainName: str
    trainNameEn: str
    transportType: str
    originName: str
    initialStationName: str
    originStationCode: str
    originStationInfo: Station
    initialTrainStationCode: str
    initialTrainStationCnsiCode: str
    destinationName: str
    finalStationName: str
    destinationStationCode: str
    destinationStationInfo: Station
    finalTrainStationCode: str
    finalTrainStationCnsiCode: str
    destinationNames: list[str]
    finalStationNames: list[str]
    departureDateTime: str
    localDepartureDateTime: str
    arrivalDateTime: str
    localArrivalDateTime: str
    arrivalDateTimes: list[str]
    localArrivalDateTimes: list[str]
    departureDateFromFormingStation: str
    departureStopTime: int
    arrivalStopTime: int
    tripDuration: float
    tripDistance: int
    isSuburban: bool
    isComponent: bool
    carServices: list
    isSaleForbidden: bool
    isTicketPrintRequiredForBoarding: bool
    bookingSystem: str
    isVrStorageSystem: bool
    placesStorageType: str
    boardingSystemTypes: list[str]
    trainBrandCode: str


class Train(TrainPreview):
    model_config = model_config
    
    carGroups: list[CarGroup]
    isFromSchedule: bool
    isTourPackagePossible: bool
    carTransportationsFreePlacesCount: None
    actualMovement: ActualMovement
    categoryId: None
    scheduleId: None
    provider: str
    hasElectronicRegistration: bool
    hasCarTransportationCoaches: bool
    hasDynamicPricingCars: bool
    hasTwoStoreyCars: bool
    hasSpecialSaleMode: bool
    carriers: list[str]
    carrierDisplayNames: list[str]
    id: int
    isBranded: bool
    destinationStationName: str
    originStationName: str