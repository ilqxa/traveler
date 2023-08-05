from pydantic import BaseModel, ConfigDict, Field

from src.objects.rzd import model_config


class ErrorInfo(BaseModel):
    model_config = model_config
    
    providerError: None
    code: int
    message: str
    messageParams: list


class QueryError(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    errorInfo: ErrorInfo
    trains: list = Field(alias='Trains')