from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user_model import User
from app.schemas.auth_schema import UserRegister
from app.auth.security import get_password_hash, verify_password

def register_new_user(db: Session, user_data: UserRegister):
    # Verificar si el email ya existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya se encuentra registrado."
        )
    
    # Encriptar la contraseña antes de guardarla
    hashed_pwd = get_password_hash(user_data.password)
    
    # Crear la instancia del modelo
    db_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pwd,
        role=user_data.role,
        is_active=True
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user