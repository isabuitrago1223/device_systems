from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.auth_schema import UserRegister, Token
from app.auth.auth_service import register_new_user, authenticate_user
from app.auth.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    db_user = register_new_user(db, user_data)
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="El correo electrónico ya se encuentra registrado."
        )
    return {"message": "Usuario registrado con éxito"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generar el Token JWT real usando los datos del usuario
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    
    # Retorna la estructura exacta que Swagger necesita para cerrar el candado
    return {"access_token": access_token, "token_type": "bearer"}