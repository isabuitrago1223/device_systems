from fastapi import APIRouter, HTTPException, Response
from typing import Optional

from app.schemas.user_schema import User, UserResponse

router = APIRouter()

users_db = [
    {
        "id": 1,
        "name": "Isabella Buitrago",
        "email": "isabella@gmail.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Lucas Ospina",
        "email": "lucas@gmail.com",
        "role": "user",
        "is_active": False
    }                          
    
]


@router.get("/users", response_model=list[UserResponse])
def get_users(
    response: Response,
    role: Optional[str] = None,
    is_active: Optional[bool] = None
):

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    result = users_db

    if role:
        result = [u for u in result if u["role"] == role]

    if is_active is not None:
        result = [u for u in result if u["is_active"] == is_active]

    return result


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, response: Response):

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    for user in users_db:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


@router.post("/users", response_model=UserResponse)
def create_user(user: User, response: Response):

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    for existing_user in users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="El correo ya existe"
            )

    users_db.append(user.model_dump())

    return user