from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    operation = Column(String, nullable=False)
    result = Column(Float, nullable=False)

Base.metadata.create_all(engine)
