from fastapi import APIRouter

from api.v1.endpoints import transformes

api_router = APIRouter()

api_router.include_router(transformes.router, prefix="/personagens", tags=["Personagem"])