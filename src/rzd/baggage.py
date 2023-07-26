from pydantic import BaseModel, field_validator


class BaggageType(BaseModel):
    Type: str | None
    Name: str | None
    Description: str | None
    CarBaggageInfo: str | None