from sqlalchemy.orm import Session
from datetime import datetime

from app.models.loan_model import Loan
from app.models.user_model import User
from app.models.device_model import Device


def get_loans(db: Session):
    return db.query(Loan).all()


def get_loan_by_id(db: Session, loan_id: int):
    return db.query(Loan).filter(
        Loan.id == loan_id
    ).first()


def create_loan(db: Session, loan_data: dict):

    user = db.query(User).filter(
        User.id == loan_data["user_id"]
    ).first()

    if not user:
        return "USER_NOT_FOUND"

    device = db.query(Device).filter(
        Device.id == loan_data["device_id"]
    ).first()

    if not device:
        return "DEVICE_NOT_FOUND"

    if not device.is_available:
        return "DEVICE_NOT_AVAILABLE"

    loan = Loan(**loan_data)

    db.add(loan)

    device.is_available = False

    db.commit()
    db.refresh(loan)

    return loan


def return_loan(
    db: Session,
    loan_id: int
):
    loan = db.query(Loan).filter(
        Loan.id == loan_id
    ).first()

    if not loan:
        return "LOAN_NOT_FOUND"

    if loan.status == "returned":
        return "ALREADY_RETURNED"

    loan.status = "returned"
    loan.return_date = datetime.utcnow()

    device = db.query(Device).filter(
        Device.id == loan.device_id
    ).first()

    if device:
        device.is_available = True

    db.commit()
    db.refresh(loan)

    return loan

def get_loans_by_device_type(
    db: Session,
    device_type: str
):
    return (
        db.query(Loan)
        .join(Device)
        .filter(
            Device.device_type == device_type
        )
        .all()
    )


def get_loans_by_user(
    db: Session,
    user_id: int
):
    return db.query(Loan).filter(
        Loan.user_id == user_id
    ).all()


def get_loans_by_device(
    db: Session,
    device_id: int
):
    return db.query(Loan).filter(
        Loan.device_id == device_id
    ).all()