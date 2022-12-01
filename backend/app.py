from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from . import models
from . import serializers
import os

mode = os.environ.get('APP_BACKEND_ENV','dev')
if mode.lower() == 'dev':
    app = FastAPI()
    def get_db():
        engine = create_engine('sqlite:///../app.db')
        yield Session(engine)
else:
    app = FastAPI(openapi_url=None)
    def get_db():
        engine = create_engine('sqlite:///./app.db')
        yield Session(engine)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoints
@app.get('/session', response_model=list[serializers.Session])
def get_all_sessions(db: Session = Depends(get_db)):
    data = db.query(models.Session).all()
    return data

@app.post("/session")
def create_session(session: serializers.SessionNew, db: Session = Depends(get_db)):
    # TODO return new object id
    data = session.__dict__
    print(data)
    new_obj = models.Session(**data)
    db.add(new_obj)
    db.commit()
    return {'id':new_obj.id}

@app.get("/session/{id}", response_model=serializers.Session)
def get_session(id:int, db: Session = Depends(get_db)):
    obj = db.get(models.Session, id)
    if not obj:
        raise HTTPException(404, 'session id not found')
    return obj

@app.put("/session/{id}")
def update_session(data: serializers.SessionUpdate, id:int, db: Session = Depends(get_db)):
    data = data.__dict__
    obj = db.get(models.Session,id)
    if not obj:
        raise HTTPException(404, 'session id not found')

    delta = data['end_time']-obj.start_time
    obj.hours = delta.total_seconds()/3600
    obj.end_time = data['end_time']
    db.commit()

    
