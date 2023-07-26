import argparse

from src.objects.rzd.suggests import Suggests
from src.processors.rzd.parsing import make_a_request
from src.queries.rzd.suggests import SuggestsRequest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='find_city_code',
        description='Enter the city name and get codes'
    )
    parser.add_argument('city_name', help='enter the city name', type=str)
    args = parser.parse_args()
    
    req = SuggestsRequest.model_validate({'params': {'Query': args.city_name}})
    res = make_a_request(req)
    
    if not isinstance(res, Suggests): raise TypeError()
    for c in res.city:
        print(f'{c.name} - {c.expressCode}')