from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.dependencies.database_dependency import get_db

from app.schemas.loan_schema import (
    LoanCreate,
    LoanResponse
)

from app.services.loan_service import (
    get_loans,
    get_loan_by_id,
    create_loan,
    return_loan,
    get_loans_by_device_type,
    get_loans_by_user,
    get_loans_by_device
)

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


@router.get(
    "",
    response_model=list[LoanResponse]
)
def get_all_loans(
    status: Optional[str] = None,
    device_type: Optional[str] = None,
    db: Session = Depends(get_db)
):

    loans = get_loans(db)

    if status:
        loans = [
            loan
            for loan in loans
            if loan.status == status
        ]

    if device_type:
        loans = get_loans_by_device_type(
            db,
            device_type
        )

    return loans


@router.get(
    "/user/{user_id}",
    response_model=list[LoanResponse]
)
def get_user_loans(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_loans_by_user(
        db,
        user_id
    )


@router.get(
    "/device/{device_id}",
    response_model=list[LoanResponse]
)
def get_device_loans(
    device_id: int,
    db: Session = Depends(get_db)
):
    return get_loans_by_device(
        db,
        device_id
    )


@router.get(
    "/{loan_id}",
    response_model=LoanResponse
)
def get_one_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):
    loan = get_loan_by_id(
        db,
        loan_id
    )

    if not loan:
        raise HTTPException(
            status_code=404,
            detail="Préstamo no encontrado"
        )

    return loan


@router.post(
    "",
    response_model=LoanResponse,
    status_code=201
)
def create_new_loan(
    loan: LoanCreate,
    db: Session = Depends(get_db)
):

    result = create_loan(
        db,
        loan.model_dump()
    )

    if result == "USER_NOT_FOUND":
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    if result == "DEVICE_NOT_FOUND":
        raise HTTPException(
            status_code=404,
            detail="Dispositivo no encontrado"
        )

    if result == "DEVICE_NOT_AVAILABLE":
        raise HTTPException(
            status_code=409,
            detail="Dispositivo no disponible"
        )

    return result


@router.patch(
    "/{loan_id}/return",
    response_model=LoanResponse
)
def return_device(
    loan_id: int,
    db: Session = Depends(get_db)
):

    result = return_loan(
        db,
        loan_id
    )

    if result == "LOAN_NOT_FOUND":
        raise HTTPException(
            status_code=404,
            detail="Préstamo no encontrado"
        )

    if result == "ALREADY_RETURNED":
        raise HTTPException(
            status_code=409,
            detail="El préstamo ya fue devuelto"
        )

    return result