from fastapi import FastAPI
from app.routes.user_routes import router

app = FastAPI(
    title="device_systems API",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Bienvenido a Device Systems API"}

app.include_router(router)