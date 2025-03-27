from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)
#Criar uma engine assíncrona para permitir que a API se comunique com o banco de dados de forma eficiente, 
# utilizando sessões assíncronas para otimizar as operações de leitura e escrita sem bloquear a aplicação
Session: AsyncEngine = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)