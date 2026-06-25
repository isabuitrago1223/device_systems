from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from typing import Optional

class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, description="Nombre completo del usuario")
    email: EmailStr = Field(..., description="Correo electrónico único y válido")
    password: str = Field(..., description="Contraseña segura")
    role: str = Field(default="user", description="Rol del usuario: admin, support, user")

    # Validación avanzada de contraseña requerida por la guía
    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if " " in value:
            raise ValueError("La contraseña no debe contener espacios en blanco.")
        if len(value) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres.")
        if not any(char.isupper() for char in value):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
        if not any(char.islower() for char in value):
            raise ValueError("La contraseña debe contener al menos una letra minúscula.")
        if not any(char.isdigit() for char in value):
            raise ValueError("La contraseña debe contener al menos un número.")
        return value

    # Validación de roles permitidos
    @field_validator("role")
    @classmethod
    def validate_role(cls, value: str) -> str:
        allowed_roles = ["admin", "support", "user"]
        if value not in allowed_roles:
            raise ValueError(f"Rol no permitido. Los roles válidos son: {', '.join(allowed_roles)}")
        return value


class UserLogin(BaseModel):
    username: str = Field(..., description="Para OAuth2 de FastAPI se usa el campo username (será el email)")
    password: str = Field(..., description="Contraseña en texto plano")


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None