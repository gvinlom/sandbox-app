from pydantic import BaseModel, root_validator
from typing import Any
from datetime import datetime as dt
import datetime


class Session(BaseModel):
    id: str
    start_time: Any
    end_time: Any
    hours: float

    class Config:
        orm_mode=True

class SessionNew(BaseModel):
    start_time: str
    end_time: Any = None
    hours: float = 0

    @root_validator
    # TODO move to frontend handler
    def convert_date(cls, values) -> datetime:
        values['start_time'] = dt.fromisoformat(values['start_time'])

        return values

    class Config:
        orm_mode=True

class SessionUpdate(BaseModel):
    end_time: str

    @root_validator
    # TODO move to frontend handler
    def convert_date(cls, values) -> datetime:
        values['end_time'] = dt.fromisoformat(values['end_time'])

        return values

    class Config:
        orm_mode=True


class Sessions(BaseModel):
    sessions: list[Session] = []

    class Config:
        orm_mode=True
