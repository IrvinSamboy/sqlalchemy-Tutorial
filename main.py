from .db import db, tables
from sqlalchemy.orm import Session


with Session(db.engine) as session:
    admin = tables.Roles(
        roleName = "admin"
    )

    user = tables.Roles(
        roleName = "user"
    )

    jose = tables.User(
        firstName = "Jose",
        lastName = "Antonio",
        role= 0
    )

    carlos = tables.User(
        firstName = "Carlos",
        lastName = "Alexander",
        role= 1
    )

    session.add_all([admin, user, jose, carlos])

    session.commit()
