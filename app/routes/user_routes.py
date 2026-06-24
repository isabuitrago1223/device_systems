from fastapi import APIRouter, HTTPException, Response, Depends
from typing import Optional

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.services.user_service import (
    get_users,
    get_user_by_id,
    create_user,
    delete_user,
    email_exists,
    update_user
)

from app.dependencies.user_dependencies import get_user_or_404

router = APIRouter()


# ==========================
# GET ALL USERS
# ==========================
@router.get(
    "/users",
    response_model=list[UserResponse],
    tags=["Users"],
    summary="Obtener todos los usuarios",
    description="Retorna la lista completa de usuarios. Permite filtrar por rol y estado."
)
def get_all_users(
    response: Response,
    role: Optional[str] = None,
    is_active: Optional[bool] = None
):

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "2.0"

    users = get_users()

    if role:
        users = [u for u in users if u["role"] == role]

    if is_active is not None:
        users = [u for u in users if u["is_active"] == is_active]

    return users


# ==========================
# GET USER BY ID
# ==========================
@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Buscar usuario por ID",
    description="Obtiene un usuario específico usando su ID."
)
def get_user(
    user: dict = Depends(get_user_or_404)
):

    return user


# ==========================
# CREATE USER
# ==========================
@router.post(
    "/users",
    response_model=UserResponse,
    status_code=201,
    tags=["Users"],
    summary="Crear usuario",
    description="Registra un nuevo usuario."
)
def create(
    user: UserCreate
):

    if email_exists(user.email):
        raise HTTPException(
            status_code=400,
            detail="Correo ya registrado"
        )

    new_user = user.model_dump()

    new_user["id"] = len(get_users()) + 1

    return create_user(new_user)


# ==========================
# PUT USER
# ==========================
@router.put(
    "/users/{user_id}",
    response_model=UserResponse,
    status_code=200,
    tags=["Users"],
    summary="Actualizar usuario completo",
    description="Reemplaza completamente la información de un usuario."
)
def update_complete_user(
    user_id: int,
    user_data: UserCreate
):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    if (
        user_data.email != user["email"]
        and email_exists(user_data.email)
    ):
        raise HTTPException(
            status_code=400,
            detail="Correo ya registrado"
        )

    updated_user = update_user(
        user_id,
        user_data.model_dump()
    )

    return updated_user


# ==========================
# PATCH USER
# ==========================
@router.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    status_code=200,
    tags=["Users"],
    summary="Actualizar parcialmente un usuario",
    description="Permite modificar uno o varios campos del usuario."
)
def update_partial_user(
    user_id: int,
    user_data: UserUpdate
):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    update_data = user_data.model_dump(
        exclude_unset=True
    )

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Debe enviar al menos un campo para actualizar"
        )

    updated_user = update_user(
        user_id,
        update_data
    )

    return updated_user


# ==========================
# DELETE USER
# ==========================
@router.delete(
    "/users/{user_id}",
    status_code=200,
    tags=["Users"],
    summary="Eliminar usuario",
    description="Elimina un usuario existente."
)
def delete(
    user: dict = Depends(get_user_or_404)
):

    delete_user(user["id"])

    return {
        "message": "Usuario eliminado correctamente"
    }