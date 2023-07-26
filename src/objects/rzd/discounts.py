from pydantic import BaseModel, field_validator

from src.objects.rzd import model_config


class Discount(BaseModel):
    model_config = model_config
    
    discountType: str
    description: str