from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.device_model import Device


def get_devices(
    db: Session,
    device_type=None,
    brand=None,
    is_available=None,
    search=None
):
    query = db.query(Device)

    if device_type:
        query = query.filter(
            Device.device_type == device_type
        )

    if brand:
        query = query.filter(
            Device.brand.ilike(f"%{brand}%")
        )

    if is_available is not None:
        query = query.filter(
            Device.is_available == is_available
        )

    if search:
        query = query.filter(
            or_(
                Device.name.ilike(f"%{search}%"),
                Device.serial_number.ilike(f"%{search}%")
            )
        )

    return query.all()


def get_device_by_id(
    db: Session,
    device_id: int
):
    return db.query(Device).filter(
        Device.id == device_id
    ).first()


def get_device_by_serial(
    db: Session,
    serial_number: str
):
    return db.query(Device).filter(
        Device.serial_number == serial_number
    ).first()


def create_device(
    db: Session,
    device_data: dict
):
    device = Device(**device_data)

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


def update_device(
    db: Session,
    device_id: int,
    data: dict
):
    device = get_device_by_id(
        db,
        device_id
    )

    if not device:
        return None

    for key, value in data.items():
        setattr(device, key, value)

    db.commit()
    db.refresh(device)

    return device


def delete_device(
    db: Session,
    device_id: int
):
    device = get_device_by_id(
        db,
        device_id
    )

    if not device:
        return False

    db.delete(device)
    db.commit()

    return True