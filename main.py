from sqlalchemy import create_engine, column, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Roles(Base):
    __tablename__ - "roles"

    idRole: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    roleName: Mapped[str] = mapped_column(String(100), nullable=False)

