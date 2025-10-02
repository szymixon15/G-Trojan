from dataclasses import dataclass


@dataclass
class CreateUserCommand:
    firstname: str
    lastname: str
