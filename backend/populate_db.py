from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import models
from datetime import datetime as dt


engine = create_engine('sqlite:///./app.db',echo=True)
models.Base.metadata.create_all(engine)

with Session(engine) as db:
    s1 = models.Session(start_time=dt(year=2022,month=1,day=1),
     end_time=dt(year=2022,month=1,day=1),hours=3)
    
    db.add(s1)
    db.commit()