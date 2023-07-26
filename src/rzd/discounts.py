from pydantic import BaseModel, field_validator

from src.rzd import model_config


class Discount(BaseModel):
    model_config = model_config
    
    discountType: str
    description: str