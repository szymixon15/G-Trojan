from pydantic import BaseModel


class CreateUserResponseDto(BaseModel):
    id: int
    firstname: str
    lastname: str