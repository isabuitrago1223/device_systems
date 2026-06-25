from fastapi import FastAPI

from app.database.connection import engine, Base

from app.routes.user_routes import router as user_router
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router

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


app.include_router(user_router)
app.include_router(device_router)
app.include_router(loan_router)