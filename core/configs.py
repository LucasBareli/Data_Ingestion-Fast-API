from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    #automatico
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/transformers"
    DBBaseModel = declarative_base()
    
class Config:
    case_sensitive = Falseenv_file = "env"
    
settings = Settings()        
