from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import EntityBase, SqlAlchemyBase

    
class Address(EntityBase, SqlAlchemyBase):
    __tablename__ = "Addresses"

    street: Mapped[str] = mapped_column(Text, nullable=False)
    city: Mapped[str] = mapped_column(Text, nullable=False)
    userid: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    user: Mapped["User"] = relationship("User", back_populates="addresses")

class User(EntityBase, SqlAlchemyBase):
    __tablename__ = "Users"

    age: Mapped[int] = mapped_column(Integer, nullable=True)
    firstname: Mapped[str] = mapped_column(String(200))
    lastname: Mapped[str] = mapped_column(String(200))
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="user")
