from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config, split_numbers_list


class FreePlacesByCompartment(BaseModel):
    model_config = model_config
    
    compartmentNumber: str
    places: list[str]
    
    split_codes = field_validator('places', mode='before')(split_numbers_list)