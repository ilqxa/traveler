from datetime import date, timedelta

from src.objects.opt.nodes import PathPoint
from src.objects.rzd.prices import CarPricing, TrainPricing
from src.processors.rzd.requesting import execute_request
from src.queries.rzd.car_pricing import (CarPricingRequest,
                                         CarPricingRequestPayload)
from src.queries.rzd.train_pricing import (TrainPricingRequest,
                                           TrainPricingRequestPayload)


def prepare_train_requests(
    pointFrom: str,
    pointTo: str,
    dateFrom: date,
    dateTo: date,
    dateFormat: str = '%Y-%m-%dT00:00:00',
) -> set[TrainPricingRequest]:
    return {
        TrainPricingRequest(
            json=TrainPricingRequestPayload(
                Origin=pointFrom,
                Destination=pointTo,
                DepartureDate=(dateFrom + timedelta(days=d)).strftime(
                    dateFormat
                ),
            )
        )  # type: ignore
        for d in range((dateTo - dateFrom).days + 1)
    }


def prepare_car_requests(
    trainPricing: TrainPricing,
    dateFormat: str = '%Y-%m-%dT00:00:00',
) -> set[CarPricingRequest]:
    return {
        CarPricingRequest(
            json=CarPricingRequestPayload(
                OriginCode=t.originStationCode,
                DestinationCode=t.destinationStationCode,
                DepartureDate=t.departureDateTime.strftime(dateFormat),
                TrainNumber=t.trainNumber,
            )
        ) # type: ignore
        for t in trainPricing.trains
    }