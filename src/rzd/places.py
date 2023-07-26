from pydantic import BaseModel, field_validator

from src.rzd import model_config


class FreePlacesByCompartment(BaseModel):
    model_config = model_config
    
    compartmentNumber: str
    places: list[str]