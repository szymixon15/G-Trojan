from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.use_cases.address.create_address.create_address_response_dto import CreateAddressResponseDto
from src.api.fast_api.exception_converter import convert_to_http_exception
from src.infrastructure.database import get_db
from src.use_cases.address.create_address.create_address_command import CreateAddressCommand
from src.use_cases.address.create_address.create_address_use_case import CreateAddressUseCase

router = APIRouter(prefix="/addresses")

@router.post(
    "/",
    response_model=CreateAddressResponseDto
)
async def create_address(
        address: CreateAddressCommand,
        session: Session = Depends(get_db)
):

    handler = CreateAddressUseCase(
        session,
        address
    )

    try:
        new_address = handler.execute()
    except Exception as e:
        raise convert_to_http_exception(e)

    return new_address

