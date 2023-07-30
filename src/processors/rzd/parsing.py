from typing import Any

import requests
from requests import Session
from requests import RequestException

from src.queries.rzd.car_pricing import CarPricingRequest
from src.queries.rzd.suggests import SuggestsRequest
from src.queries.rzd.train_pricing import TrainPricingRequest


def make_a_request(
    req: SuggestsRequest | TrainPricingRequest | CarPricingRequest,
    session: Session | None = None
) -> SuggestsRequest.responseType | TrainPricingRequest.responseType | CarPricingRequest.responseType:
    if not session: session = Session()
    requestData = req.model_dump(by_alias=True)
    
    respRaw = session.request(**requestData)
    if respRaw.status_code != 200: raise RequestException()
    
    respParsed = req.responseType.model_validate_json(respRaw.text)
    session.close()
    return respParsed