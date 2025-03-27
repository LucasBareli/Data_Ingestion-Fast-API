from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.transformes_models import TransformesModel
from schemas.transformes_schema import TransformesSchema
from core.deps import get_session


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransformesSchema)
async def post_transformers(transformers: TransformesSchema, db: AsyncSession = Depends(get_session)):
    novo_personagem = TransformesModel(
        nome = transformers.nome, 
        motor = transformers.motor, 
        time = transformers.time, 
        tipo_transporte = transformers.tipo_transporte, 
        idade = transformers.idade, 
        cor = transformers.cor, 
        foto = transformers.foto
        )
    
    db.add(novo_personagem)
    await db.commit()

    return novo_personagem


@router.get("/", response_model=List[TransformesSchema])
async def get_transformers(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TransformesModel)
        result = await session.execute(query)
        personagens: List[TransformesModel] = result.scalars().all()

        return personagens


@router.get("/{transformer_id}", response_model=TransformesSchema)
async def get_transforme(transformer_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query =  select(TransformesModel).filter(TransformesModel.id == transformer_id)
        result = await session.execute(query)
        transformer = result.scalars_one_or_none()

        if transformer:
            return transformer
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{transformer_id}", response_model=TransformesSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_transformer(transformer_id: int, transformer = TransformesSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query =  select(TransformesModel).filter(TransformesModel.id == transformer_id)
        result = await session.execute(query)
        transformer_up = result.scalars_one_or_none()
        
        if transformer_up:
            transformer_up. nome = transformer.nome
            transformer_up.motor = transformer.motor
            transformer_up.time = transformer.time
            transformer_up.tipo_transporte = transformer.tipo_transporte
            transformer_up.idade = transformer.idade
            transformer_up.cor = transformer.cor
            transformer_up.foto = transformer.foto

            await session.commit()
            return transformer_up
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)


#Há outro metodo, porem tem que mecher no schemas
"""@router.patch("/{transformer_id}", response_model=TransformesSchema, status_code=status.HTTP_202_ACCEPTED)
async def patch_transformer(transformer_id: int, transformer: TransformesSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TransformesModel).filter(TransformesModel.id == transformer_id)
        result = await session.execute(query)
        transformer_patch = result.scalars_one_or_none()

        if transformer_patch:
            if transformer.nome is not None:
                transformer_patch.nome = transformer.nome
            if transformer.motor is not None:
                transformer_patch.motor = transformer.motor
            if transformer.time is not None:
                transformer_patch.time = transformer.time
            if transformer.tipo_transporte is not None:
                transformer_patch.tipo_transporte = transformer.tipo_transporte
            if transformer.idade is not None:
                transformer_patch.idade = transformer.idade
            if transformer.cor is not None:
                transformer_patch.cor = transformer.cor
            if transformer.foto is not None:
                transformer_patch.foto = transformer.foto

            await session.commit()

            return transformer_patch
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)"""


@router.delete("/{transformers_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transformer(transformer_id: int, db: AsyncSession= Depends(get_session)):
    async with db as session:
        query =  select(TransformesModel).filter(TransformesModel.id == transformer_id)
        result = await session.execute(query)
        transformer_del = result.scalars_one_or_none()

        if transformer_del:
            await session.delete(transformer_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)