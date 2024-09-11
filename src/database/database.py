from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.config_dotenv import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()




