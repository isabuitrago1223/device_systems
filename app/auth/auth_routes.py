from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.database.connection import get_db
from app.schemas.auth_schema import UserRegister, Token
from app.auth.auth_service import register_new_user, authenticate_user
from app.auth.security import create_access_token
from app.dependencies.auth_dependency import get_current_active_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# Configuración del Rate Limiting
limiter = Limiter(key_func=get_remote_address)


# ==========================
# Registro de usuarios
# ==========================
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
@limiter.limit("3/minute")
def register(
    request: Request,
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    db_user = register_new_user(db, user_data)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya se encuentra registrado."
        )

    return {
        "message": "Usuario registrado con éxito"
    }


# ==========================
# Login
# ==========================
@router.post(
    "/login",
    response_model=Token
)
@limiter.limit("5/minute")
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ==========================
# Usuario autenticado
# ==========================
@router.get("/me")
def get_me(
    current_user=Depends(get_current_active_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active
    }