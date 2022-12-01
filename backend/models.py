from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Session(Base):
    __tablename__ = "Session"
    id = Column(Integer, primary_key=True)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP, nullable=True)
    hours = Column(Float)
