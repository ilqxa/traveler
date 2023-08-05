from datetime import datetime
from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config
from src.objects.rzd.cars import CarGroup
from src.objects.rzd.movement import ActualMovement
from src.objects.rzd.stations import Station


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
    departureDateTime: datetime
    localDepartureDateTime: datetime
    arrivalDateTime: datetime
    localArrivalDateTime: datetime
    arrivalDateTimes: list[datetime]
    localArrivalDateTimes: list[datetime]
    departureDateFromFormingStation: datetime
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
    trainBrandCode: str | None


class Train(TrainPreview):
    model_config = model_config
    
    carGroups: list[CarGroup]
    isFromSchedule: bool
    isTourPackagePossible: bool
    carTransportationsFreePlacesCount: None
    actualMovement: ActualMovement | None
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