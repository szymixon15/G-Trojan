from sqlalchemy.orm import Session

from src.core.entities.user import Address
from src.use_cases.address.create_address.create_address_command import CreateAddressCommand
from src.use_cases.address.create_address.create_address_response_dto import CreateAddressResponseDto
from src.use_cases.use_case_base import UseCaseBase


class CreateAddressUseCase(UseCaseBase):
    def __init__(self, session: Session, request: CreateAddressCommand):
        self.session = session
        self.request = request

    def execute(self):
        new_address = Address(
            street=self.request.street,
            city=self.request.city,
            userid=self.request.userid
        )

        self.session.add(new_address)
        self.session.commit()

        return CreateAddressResponseDto(
            id=new_address.id,
            street=new_address.street,
            city=new_address.city,
            userid=new_address.userid
        )

