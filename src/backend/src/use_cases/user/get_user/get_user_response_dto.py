from typing import List

from pydantic import BaseModel

class AddressDto(BaseModel):
    id: int
    street: str
    city: str

class GetUserResponseDto(BaseModel):
    id: int
    firstname: str
    lastname: str
    addresses: List[AddressDto]

