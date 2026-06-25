from fastapi import FastAPI

from app.routes.user_routes import router

from app.database.connection import engine
from app.models.user_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Device Systems API",
    description="API REST para la gestión de usuarios usando FastAPI y SQLAlchemy",
    version="3.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Bienvenido a Device Systems API"
    }

app.include_router(router)