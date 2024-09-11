from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.config_dotenv import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

Base = declarative_base()

async_engine = create_async_engine(settings.database_url)

engine = create_engine("postgresql://postgres:khoatiendao@localhost:5432/fastAPI")

SessionLocal = sessionmaker(bind=async_engine, class_= AsyncSession, expire_on_commit=False)



async def get_async_session() -> AsyncSession: # type: ignore
    async with SessionLocal() as session:
        yield session  # This will be used in the dependency





