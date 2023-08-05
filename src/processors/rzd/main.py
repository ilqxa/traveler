from datetime import date

from src.objects.opt.nodes import PathPoint
from src.objects.opt.places import TrainPlace
from src.objects.rzd.prices import CarPricing, TrainPricing
from src.processors.rzd.parsing import (car_pricing_to_places,
                                        points_to_city_codes)
from src.processors.rzd.preparing import (prepare_car_requests,
                                          prepare_train_requests)
from src.processors.rzd.requesting import execute_request


def get_available_places(
    nodes: set[PathPoint],
    dateFrom: date,
    dateTo: date,
) -> set[TrainPlace]:
    trainPricing: set[TrainPricing] = set()
    for pointFrom, pointTo in points_to_city_codes(nodes):    
        for q in prepare_train_requests(pointFrom, pointTo, dateFrom, dateTo):
            res = execute_request(q)
            if isinstance(res, TrainPricing):
                trainPricing.add(res)

    carPricing: set[CarPricing] = set()
    for tp in trainPricing:
        for q in prepare_car_requests(tp):
            res = execute_request(q)
            if isinstance(res, CarPricing):
                carPricing.add(res)
    
    places: set[TrainPlace] = set()
    for cp in carPricing:
        places |= car_pricing_to_places(cp)

    return places