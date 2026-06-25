import os
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-default")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Configuración de passlib para usar bcrypt en las contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# --- Funciones de Hash para Contraseñas ---

def get_password_hash(password: str) -> str:
    """Recibe la contraseña en texto plano y retorna el hash seguro."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compara una contraseña en texto plano con el hash guardado en la BD."""
    return pwd_context.verify(plain_password, hashed_password)


# --- Funciones para Gestión de Tokens JWT ---

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Genera un token JWT firmado que expira en el tiempo configurado."""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Añadimos la fecha de expiración al contenido del token (payload)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """Decodifica un token JWT y verifica que sea válido y no haya expirado."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None