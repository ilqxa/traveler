from typing import Any

import requests
from requests import Session
from requests import RequestException

from src.queries.rzd.car_pricing import CarPricingRequest
from src.queries.rzd.suggests import SuggestsRequest
from src.queries.rzd.train_pricing import TrainPricingRequest

allowedRequests = SuggestsRequest | TrainPricingRequest | CarPricingRequest
allowedResponses = SuggestsRequest.responseType | TrainPricingRequest.responseType | CarPricingRequest.responseType

def make_a_request(req: allowedRequests, session: Session | None = None) -> allowedResponses:
    if not session: session = Session()
    requestData = req.model_dump(exclude={'responseType'}, by_alias=True)
    
    respRaw = session.request(**requestData)
    if respRaw.status_code != 200: raise RequestException()
    
    respParsed = req.responseType.model_validate_json(respRaw.text)
    session.close()
    return respParsed