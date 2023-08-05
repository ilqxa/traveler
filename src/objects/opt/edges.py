from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.objects.opt.nodes import PathPoint
from src.objects.opt.places import TrainPlace


class PathSection(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    nodeFrom: PathPoint
    nodeTo: PathPoint
    timeFrom: datetime
    timeTo: datetime
    
    seats: set[TrainPlace]