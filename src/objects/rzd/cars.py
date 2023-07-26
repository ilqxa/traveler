from datetime import datetime

from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config
from src.objects.rzd.baggage import BaggageType
from src.objects.rzd.discounts import Discount
from src.objects.rzd.places import FreePlacesByCompartment


class CarGroup(BaseModel):
    model_config = model_config
    
    carriers: list[str]
    carrierDisplayNames: list[str]
    serviceClasses: list[str]
    minPrice: float
    maxPrice: float
    carType: str
    carTypeName: str
    placeQuantity: int
    lowerPlaceQuantity: int
    upperPlaceQuantity: int
    lowerSidePlaceQuantity: int
    upperSidePlaceQuantity: int
    malePlaceQuantity: int
    femalePlaceQuantity: int
    emptyCabinQuantity: int
    mixedCabinQuantity: int
    isSaleForbidden: bool
    availabilityIndication: str
    carDescriptions: list[str]
    serviceClassNameRu: str | None
    serviceClassNameEn: str | None
    internationalServiceClasses: list[str]
    serviceCosts: list[float]
    isBeddingSelectionPossible: bool
    boardingSystemTypes: list[str]
    hasElectronicRegistration: bool
    hasGenderCabins: bool
    hasPlaceNumeration: bool
    hasPlacesNearPlayground: bool
    hasPlacesNearPets: bool
    hasPlacesForDisabledPersons: bool
    hasPlacesNearBabies: bool
    availableBaggageTypes: list[BaggageType]
    hasNonRefundableTariff: bool
    discounts: list[Discount]
    infoRequestSchema: str
    totalPlaceQuantity: int
    placeReservationTypes: list[str]
    isThreeHoursReservationAvailable: bool
    isMealOptionPossible: bool
    isAdditionalMealOptionPossible: bool
    isOnRequestMealOptionPossible: bool
    isTransitDocumentRequired: bool
    isInterstate: bool
    clientFeeCalculation: None
    agentFeeCalculation: None
    hasNonBrandedCars: bool
    tripPointQuantity: int
    hasPlacesForBusinessTravelBooking: bool
    serviceClassName: str
    hasFssBenefit: bool


class Car(BaseModel):
    destinationStationCode: str
    carType: str
    carDirection: str
    railwayCarSchemeId: None
    carSubType: str
    carTypeName: str
    carSchemeName: str
    carNumber: str
    serviceClass: str
    serviceClassNameRu: str | None
    serviceClassNameEn: str | None
    internationalServiceClass: str
    carDescription: str
    serviceClassTranscript: str
    freePlaces: list[str]
    freePlacesByCompartments: list[FreePlacesByCompartment]
    placeQuantity: int
    isTwoStorey: bool
    services: list[str]
    petTransportationShortDescription: None
    petTransportationFullDescription: None
    minPrice: float
    maxPrice: float
    serviceCost: float
    placeReservationType: str
    carrier: str
    carrierDisplayName: str
    hasGenderCabins: bool
    rzhdCardTypes: list[str]
    trainNumber: str
    arrivalDateTime: datetime
    localArrivalDateTime: datetime
    hasNoInterchange: bool
    hasPlaceNumeration: bool
    isBeddingSelectionPossible: bool
    hasElectronicRegistration: bool
    hasDynamicPricing: bool
    hasPlacesNearBabies: bool
    hasPlacesNearPlayground: bool
    hasPlacesNearPets: bool
    hasNonRefundableTariff: bool
    onlyNonRefundableTariff: bool
    isAdditionalPassengerAllowed: bool
    isChildTariffTypeAllowed: bool
    carPlaceType: str
    carPlaceCode: str
    carPlaceNameRu: str
    carPlaceNameEn: str
    discounts: list[Discount]
    isSaleForbidden: bool
    availabilityIndication: str
    isThreeHoursReservationAvailable: bool
    road: str
    infoRequestSchema: str
    passengerSpecifyingRules: str
    isMealOptionPossible: bool
    isAdditionalMealOptionPossible: bool
    isOnRequestMealOptionPossible: bool
    mealSalesOpenedTill: str
    isTransitDocumentRequired: bool
    isInterstate: bool
    clientFeeCalculation: None
    agentFeeCalculation: None
    isBranded: bool
    isBuffet: bool
    tripDirection: str
    isForDisabledPersons: bool
    isSpecialSaleMode: bool
    boardingSystemType: str
    availableBaggageTypes: list[BaggageType]
    isTourPackageAvailable: bool
    arePlacesForBusinessTravelBooking: bool
    carPlaceName: str
    hasFssBenefit: bool
    serviceClassName: str