from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Calculation(Base):
    __tablename__ = 'calculations'  # Ensure this matches the table name used in your program
    id = Column(Integer, primary_key=True)
    operation = Column(String)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Database setup
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)  # This creates the table if it doesn't exist
