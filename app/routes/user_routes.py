from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserPatch,
    UserResponse
)

from app.services.user_service import (
    get_users,
    get_user_by_id,
    get_user_by_email,
    create_user,
    update_user,
    delete_user
)

from app.dependencies.database_dependency import get_db

router = APIRouter()


# ==========================
# GET ALL USERS
# ==========================
@router.get(
    "/users",
    response_model=list[UserResponse],
    tags=["Users"],
    summary="Obtener todos los usuarios"
)
def get_all_users(
    response: Response,
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "3.0"

    users = get_users(db)

    if role:
        users = [user for user in users if user.role == role]

    if is_active is not None:
        users = [
            user for user in users
            if user.is_active == is_active
        ]

    return users


# ==========================
# GET USER BY ID
# ==========================
@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Buscar usuario por ID"
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return user


# ==========================
# CREATE USER
# ==========================
@router.post(
    "/users",
    response_model=UserResponse,
    status_code=201,
    tags=["Users"],
    summary="Crear usuario"
)
def create(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Correo ya registrado"
        )

    return create_user(
        db,
        user.model_dump()
    )


# ==========================
# PUT USER
# ==========================
@router.put(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Actualizar usuario completo"
)
def update_complete_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    email_user = get_user_by_email(
        db,
        user_data.email
    )

    if email_user and email_user.id != user_id:
        raise HTTPException(
            status_code=400,
            detail="Correo ya registrado"
        )

    return update_user(
        db,
        user_id,
        user_data.model_dump()
    )


# ==========================
# PATCH USER
# ==========================
@router.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Actualizar parcialmente un usuario"
)
def update_partial_user(
    user_id: int,
    user_data: UserPatch,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(
        db,
        user_id
    )

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
            detail="Debe enviar al menos un campo"
        )

    if "email" in update_data:

        email_user = get_user_by_email(
            db,
            update_data["email"]
        )

        if email_user and email_user.id != user_id:
            raise HTTPException(
                status_code=400,
                detail="Correo ya registrado"
            )

    return update_user(
        db,
        user_id,
        update_data
    )


# ==========================
# DELETE USER
# ==========================
@router.delete(
    "/users/{user_id}",
    status_code=200,
    tags=["Users"],
    summary="Eliminar usuario"
)
def delete(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_user(
        db,
        user_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "message": "Usuario eliminado correctamente"
    }