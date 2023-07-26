from pydantic import BaseModel, ConfigDict

from src.objects.rzd import model_config


class BaggageType(BaseModel):
    model_config = model_config
    
    type: str | None
    name: str | None
    description: str | None
    carBaggageInfo: str | None