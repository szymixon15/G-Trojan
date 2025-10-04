from pydantic import BaseModel


class CreateAddressResponseDto(BaseModel):
    id: int
    street: str
    city: str
    userid: int
