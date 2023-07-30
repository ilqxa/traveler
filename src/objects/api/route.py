from pydantic import BaseModel, ConfigDict


class RoutePoint(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    cityCode: str
    isFirst: bool
    isLast: bool