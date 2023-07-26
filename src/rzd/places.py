from pydantic import BaseModel, field_validator


class FreePlacesByCompartment(BaseModel):
    CompartmentNumber: str
    Places: list[str]