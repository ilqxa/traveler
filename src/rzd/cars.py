from pydantic import BaseModel, field_validator

from src.rzd.baggage import BaggageType
from src.rzd.discounts import Discount
from src.rzd.places import FreePlacesByCompartment


class CarGroup(BaseModel):
    Carriers: list[str]
    CarrierDisplayNames: list[str]
    ServiceClasses: list[str]
    MinPrice: float
    MaxPrice: float
    CarType: str
    CarTypeName: str
    PlaceQuantity: int
    LowerPlaceQuantity: int
    UpperPlaceQuantity: int
    LowerSidePlaceQuantity: int
    UpperSidePlaceQuantity: int
    MalePlaceQuantity: int
    FemalePlaceQuantity: int
    EmptyCabinQuantity: int
    MixedCabinQuantity: int
    IsSaleForbidden: bool
    AvailabilityIndication: str
    CarDescriptions: list[str]
    ServiceClassNameRu: str | None
    ServiceClassNameEn: str | None
    InternationalServiceClasses: list[str]
    ServiceCosts: list[float]
    IsBeddingSelectionPossible: bool
    BoardingSystemTypes: list[str]
    HasElectronicRegistration: bool
    HasGenderCabins: bool
    HasPlaceNumeration: bool
    HasPlacesNearPlayground: bool
    HasPlacesNearPets: bool
    HasPlacesForDisabledPersons: bool
    HasPlacesNearBabies: bool
    AvailableBaggageTypes: list[BaggageType]
    HasNonRefundableTariff: bool
    Discounts: list[Discount]
    InfoRequestSchema: str
    TotalPlaceQuantity: int
    PlaceReservationTypes: list[str]
    IsThreeHoursReservationAvailable: bool
    IsMealOptionPossible: bool
    IsAdditionalMealOptionPossible: bool
    IsOnRequestMealOptionPossible: bool
    IsTransitDocumentRequired: bool
    IsInterstate: bool
    ClientFeeCalculation: None
    AgentFeeCalculation: None
    HasNonBrandedCars: bool
    TripPointQuantity: int
    HasPlacesForBusinessTravelBooking: bool
    ServiceClassName: str
    HasFssBenefit: bool


class Car(BaseModel):
    DestinationStationCode: str
    CarType: str
    CarDirection: str
    RailwayCarSchemeId: None
    CarSubType: str
    CarTypeName: str
    CarSchemeName: str
    CarNumber: str
    ServiceClass: str
    ServiceClassNameRu: str | None
    ServiceClassNameEn: str | None
    InternationalServiceClass: str
    CarDescription: str
    ServiceClassTranscript: str
    FreePlaces: list[str]
    FreePlacesByCompartments: list[FreePlacesByCompartment]
    PlaceQuantity: int
    IsTwoStorey: bool
    Services: list[str]
    PetTransportationShortDescription: None
    PetTransportationFullDescription: None
    MinPrice: float
    MaxPrice: float
    ServiceCost: float
    PlaceReservationType: str
    Carrier: str
    CarrierDisplayName: str
    HasGenderCabins: bool
    RzhdCardTypes: list[str]
    TrainNumber: str
    ArrivalDateTime: str
    LocalArrivalDateTime: str
    HasNoInterchange: bool
    HasPlaceNumeration: bool
    IsBeddingSelectionPossible: bool
    HasElectronicRegistration: bool
    HasDynamicPricing: bool
    HasPlacesNearBabies: bool
    HasPlacesNearPlayground: bool
    HasPlacesNearPets: bool
    HasNonRefundableTariff: bool
    OnlyNonRefundableTariff: bool
    IsAdditionalPassengerAllowed: bool
    IsChildTariffTypeAllowed: bool
    CarPlaceType: str
    CarPlaceCode: str
    CarPlaceNameRu: str
    CarPlaceNameEn: str
    Discounts: list[Discount]
    IsSaleForbidden: bool
    AvailabilityIndication: str
    IsThreeHoursReservationAvailable: bool
    Road: str
    InfoRequestSchema: str
    PassengerSpecifyingRules: str
    IsMealOptionPossible: bool
    IsAdditionalMealOptionPossible: bool
    IsOnRequestMealOptionPossible: bool
    MealSalesOpenedTill: str
    IsTransitDocumentRequired: bool
    IsInterstate: bool
    ClientFeeCalculation: None
    AgentFeeCalculation: None
    IsBranded: bool
    IsBuffet: bool
    TripDirection: str
    IsForDisabledPersons: bool
    IsSpecialSaleMode: bool
    BoardingSystemType: str
    AvailableBaggageTypes: list[BaggageType]
    IsTourPackageAvailable: bool
    ArePlacesForBusinessTravelBooking: bool
    CarPlaceName: str
    HasFssBenefit: bool
    ServiceClassName: str