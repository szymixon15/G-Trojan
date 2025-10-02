from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class EntityBase:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

class SqlAlchemyBase(DeclarativeBase):
    pass