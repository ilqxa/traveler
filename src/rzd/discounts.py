from pydantic import BaseModel, field_validator


class Discount(BaseModel):
    DiscountType: str
    Description: str