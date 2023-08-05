from itertools import permutations

from src.objects.opt.edges import PathSection
from src.objects.opt.nodes import PathPoint
from src.objects.opt.requirements import TourRequirements
from src.objects.opt.places import TrainPlace
from src.objects.rzd.cars import Car
from src.objects.rzd.prices import CarPricing


def points_to_city_codes(
    nodes: set[PathPoint],
) -> set[tuple[str, str]]:
    return {
        (pointFrom.cityCode, pointTo.cityCode)
        for pointFrom, pointTo in permutations(nodes, r=2)
    }


def car_pricing_to_places(
    carPricing: CarPricing,
) -> set[TrainPlace]:
    places: set[TrainPlace] = set()
    for c in carPricing.cars:
        if c.carTypeName not in ['КУПЕ', 'ПЛАЦ']: continue
        for fpc in c.freePlacesByCompartments:
            for p in fpc.places:
                places.add(TrainPlace(
                    trainNumber = c.trainNumber,
                    carNumber = c.carNumber,
                    compartmentNumber = fpc.compartmentNumber,
                    placeNumber = p,
                    carType = c.carTypeName, # type: ignore
                    price = c.maxPrice,
                    isLower = 'нижнее' in c.carPlaceName.lower(),
                    isSide = 'боковое' in c.carPlaceName.lower(),
                    isNearToilet = 'последнее' in c.carPlaceName.lower(),
                ))
    
    return places