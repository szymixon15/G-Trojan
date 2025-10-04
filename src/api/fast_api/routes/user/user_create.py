from fastapi import APIRouter, Depends

from src.api.fast_api.exception_converter import convert_to_http_exception
from src.infrastructure.database import get_db
from src.use_cases.user.create_user.create_user_command import CreateUserCommand
from src.use_cases.user.create_user.create_user_response_dto import CreateUserResponseDto
from src.use_cases.user.create_user.create_user_use_case import CreateUserUseCase

router = APIRouter(prefix="/users")

@router.post(
    "/",
    response_model=CreateUserResponseDto
)
async def create_user(user: CreateUserCommand, session = Depends(get_db)):
    handler = CreateUserUseCase(session, user)

    try:
        new_user = handler.execute()
    except Exception as e:
        raise convert_to_http_exception(e)

    return new_user
