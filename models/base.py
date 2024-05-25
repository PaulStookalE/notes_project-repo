import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


load_dotenv()


db = create_engine(os.getenv('DATABASE'))


Session = sessionmaker(db)
session = Session()


BASE = declarative_base()


def create_db():
    BASE.metadata.create_all(db)


def drop_db():
    BASE.metadata.drop_all(db)