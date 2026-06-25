from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.dependencies.database_dependency import get_db

from app.schemas.device_schema import (
    DeviceCreate,
    DeviceUpdate,
    DeviceResponse
)

from app.services.device_service import (
    get_devices,
    get_device_by_id,
    get_device_by_serial,
    create_device,
    update_device,
    delete_device
)

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.get(
    "",
    response_model=list[DeviceResponse]
)
def get_all_devices(
    device_type: Optional[str] = None,
    brand: Optional[str] = None,
    is_available: Optional[bool] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return get_devices(
        db,
        device_type,
        brand,
        is_available,
        search
    )


@router.get(
    "/{device_id}",
    response_model=DeviceResponse
)
def get_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    device = get_device_by_id(
        db,
        device_id
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Dispositivo no encontrado"
        )

    return device


@router.post(
    "",
    response_model=DeviceResponse,
    status_code=201
)
def create_new_device(
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    existing = get_device_by_serial(
        db,
        device.serial_number
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Número de serie duplicado"
        )

    return create_device(
        db,
        device.model_dump()
    )


@router.put(
    "/{device_id}",
    response_model=DeviceResponse
)
def update_complete_device(
    device_id: int,
    device_data: DeviceCreate,
    db: Session = Depends(get_db)
):
    device = update_device(
        db,
        device_id,
        device_data.model_dump()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Dispositivo no encontrado"
        )

    return device


@router.patch(
    "/{device_id}",
    response_model=DeviceResponse
)
def update_partial_device(
    device_id: int,
    device_data: DeviceUpdate,
    db: Session = Depends(get_db)
):
    device = update_device(
        db,
        device_id,
        device_data.model_dump(
            exclude_unset=True
        )
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Dispositivo no encontrado"
        )

    return device


@router.delete(
    "/{device_id}",
    status_code=204
)
def remove_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_device(
        db,
        device_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Dispositivo no encontrado"
        )