from sqlalchemy import create_engine, column, String, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship

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

with Session(engine) as session:
    admin = Roles(
        roleName = "admin"
    )

    user = Roles(
        roleName = "user"
    )

    jose = User(
        firstName = "Jose",
        lastName = "Antonio",
        role= 0
    )

    carlos = User(
        firstName = "Carlos",
        lastName = "Alexander",
        role= 1
    )

    session.add_all([admin, user, jose, carlos])

    session.commit()
