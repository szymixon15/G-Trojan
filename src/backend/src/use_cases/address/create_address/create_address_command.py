from dataclasses import dataclass


@dataclass
class CreateAddressCommand:
    street: str
    city: str
    userid: int