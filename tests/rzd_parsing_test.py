from src.processors.rzd.parsing import make_a_request
from src.queries.rzd.suggests import SuggestsRequest


def test_request():
    r = SuggestsRequest.model_validate({'params': {'Query': 'ЯРОСЛАВЛЬ'}})
    res = make_a_request(r)
    assert True