import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
# import pymysql
from dotenv import load_dotenv

load_dotenv()

database_url = f"mysql://{os.environ['DATABASE_USER']}:@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_NAME']}"

engine = create_engine(
    database_url,
)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# meta = MetaData

Base = declarative_base()

"""TODO"""
#add config.py file
#this overwrites setting with new ones
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     app_name: str = "Awesome API"
    
#     class config:
#         env_file = ".env"





