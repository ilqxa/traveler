from datetime import date, timedelta
from typing import Any

import requests
from requests import RequestException, Session

from src.objects.rzd.errors import QueryError
from src.queries.rzd.car_pricing import CarPricingRequest
from src.queries.rzd.suggests import SuggestsRequest
from src.queries.rzd.train_pricing import TrainPricingRequest


def execute_request(
    req: SuggestsRequest | TrainPricingRequest | CarPricingRequest,
    session: Session | None = None,
) -> (
    SuggestsRequest.responseType |
    TrainPricingRequest.responseType |
    CarPricingRequest.responseType |
    QueryError
):
    if not session: session = Session()
    requestData = req.model_dump(by_alias=True)
    
    respRaw = session.request(**requestData)
    if respRaw.status_code != 200: raise RequestException()
    session.close()
    
    for respType in (req.responseType, QueryError):
        try:
            respParsed = respType.model_validate_json(respRaw.text)
        except Exception:
            continue
        else:
            break
    else:
        raise TypeError
    
    return respParsed