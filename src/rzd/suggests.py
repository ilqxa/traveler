from pydantic import BaseModel, field_validator



class Point(BaseModel):
    nodeId: str
    expressCode: str
    name: str
    nodeType: str
    transportType: str
    region: str
    regionIso: str
    countryIso: str
    aviaCode: str | None = None
    busCode: str | None = None
    suburbanCode: list[str]
    foreignCode: str
    expressCodes: list[str] | None = None
    hasAeroExpress: bool
    
    @field_validator('suburbanCode', 'expressCodes', mode='before')
    def split_codes(cls, codes: str | None) -> list[int]:
        if not codes: return []
        else: return [int(c) for c in codes.split(',')]


class Suggests(BaseModel):
    city: list[Point]
    train: list[Point]
    avia: list[Point]