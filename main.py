from sqlalchemy import create_engine, column, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Roles(Base):
    __tablename__ = "roles"

    idRole: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    roleName: Mapped[str] = mapped_column(String(100), nullable=False)

class User(Base):
    __tablename__ = "user"

    idUser: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstName: Mapped[str] = mapped_column(String(100), nullable=False)
    lastName: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[int] = mapped_column(ForeignKey("roles.idRole"))

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)