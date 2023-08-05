from pydantic import BaseModel, ConfigDict, Field


class Headers(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    userAgent: str = Field(alias='User-Agent', default='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0')
    referer: str = Field(alias='Referer', default='https://ticket.rzd.ru')
    host: str = Field(alias='Host', default='ticket.rzd.ru')
    origin: str = Field(alias='Origin', default='https://ticket.rzd.ru')
    accept: str = Field(alias='Accept', default='application/json')
    acceptLanguage: str = Field(alias='Accept-Language', default='en-US,en;q=0.9')
    contentType: str = Field(alias='Content-Type', default='application/json')


class Cookies(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    lang: str = Field(alias='lang', default='ru')
    authFlag: str = Field(alias='AuthFlag', default='false')
    langSite: str = Field(alias='LANG_SITE', default='ru')


class CommonRequest(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    headers: Headers = Field(default_factory=Headers)
    cookies: Cookies = Field(default_factory=Cookies)
    allowRedirects: bool = Field(alias='allow_redirects', default=True)
    timeout: int = Field(default=10)
    verify: bool = Field(default=False)