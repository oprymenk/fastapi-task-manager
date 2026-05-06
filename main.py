from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import tasks
from data.database import engine
from models.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(tasks.router)