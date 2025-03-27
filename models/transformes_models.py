from core.configs import settings
from sqlalchemy import Column, String, Integer, Float

class TransformesModel(settings.DBBaseModel):
    __tablename__= "Personagens"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(256))
    motor: str = Column(String(256))
    time: str = Column(String(256))
    tipo_transporte: str = Column(String(256))
    idade: int = Column(Integer())
    cor: str = Column(String(256))
    foto: str = Column(String(256))