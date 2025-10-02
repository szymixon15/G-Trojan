from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.fast_api.exception_converter import convert_to_http_exception
from src.infrastructure.database import get_db
from src.use_cases.user.get_user.get_user_query import GetUserQuery
from src.use_cases.user.get_user.get_user_response_dto import GetUserResponseDto
from src.use_cases.user.get_user.get_user_use_case import GetUserUseCase

router = APIRouter(prefix="/users")

@router.get("/{user_id}", response_model=GetUserResponseDto)
def get_user_by_id(
        user_id: int,
        session: Session = Depends(get_db)
):
    query = GetUserQuery(user_id)

    handler = GetUserUseCase(
        session,
        query
    )

    try:
        user = handler.execute()
    except Exception as e:
        raise convert_to_http_exception(e)

    return user