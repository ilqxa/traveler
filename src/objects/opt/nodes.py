from datetime import datetime, timedelta

from pydantic import BaseModel, ConfigDict


class PathPoint(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    title: str
    cityCode: str
    stayTime: datetime
    toleranceTime: timedelta