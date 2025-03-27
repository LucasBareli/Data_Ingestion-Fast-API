from typing import Optional
from pydantic import BaseModel as SCBaseModel

class TransformesSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    motor: str
    time: str
    tipo_transporte: str
    idade: int
    cor: str
    foto: str

class Config:
    orm_mode = True