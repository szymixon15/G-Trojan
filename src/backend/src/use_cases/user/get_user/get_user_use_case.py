from sqlalchemy.orm import Session

from src.core.entities.user import User
from src.use_cases.exceptions.exceptions import NotFoundError
from src.use_cases.use_case_base import UseCaseBase
from src.use_cases.user.get_user.get_user_query import GetUserQuery
from src.use_cases.user.get_user.get_user_response_dto import GetUserResponseDto, AddressDto


class GetUserUseCase(UseCaseBase):
    def __init__(
            self,
            session: Session,
            request: GetUserQuery
    ):
        self.session = session
        self.request = request


    def execute(self):
        user = self.session.get_one(User, self.request.id)

        if user is None:
            raise NotFoundError(f"User with id {self.request.id} not found")

        return GetUserResponseDto(
            id=user.id,
            firstname=user.firstname,
            lastname=user.lastname,
            addresses=[AddressDto(
                id=address.id,
                street=address.street,
                city=address.city
            ) for address in user.addresses]
        )
