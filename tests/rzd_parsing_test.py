from datetime import datetime, timedelta, date
from src.objects.opt.nodes import PathPoint
from src.processors.rzd.requesting import execute_request
from src.queries.rzd.suggests import SuggestsRequest
from src.processors.rzd.main import get_available_places


def test_request():
    r = SuggestsRequest.model_validate({'params': {'Query': 'ЯРОСЛАВЛЬ'}})
    res = execute_request(r)
    assert True


def test_cars_data():
    syk = PathPoint(
        title = 'Syktyvkar',
        cityCode = '2010280',
        stayTime = datetime(2023, 1, 1, 0, 0, 0),
        toleranceTime = timedelta(days=1)
    )
    yar = PathPoint(
        title = 'Yaroslavl',
        cityCode = '2010001',
        stayTime = datetime(2023, 1, 1, 0, 0, 0),
        toleranceTime = timedelta(days=1)
    )
    res = get_available_places({yar, syk}, date(2023, 9, 7), date(2023, 9, 7))