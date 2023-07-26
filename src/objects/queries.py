from datetime import datetime, timedelta
from pydantic import BaseModel, Field


class TaskForSearching(BaseModel):
    dateFrom: datetime = Field(default_factory=datetime.now)
    dateTo: datetime = Field(default_factory=datetime.now)
    places: list[str]