from ..db.tables import Roles
from sqlalchemy.orm import Session

def createRol(name: str, db: Session):
    rol = Roles(
        roleName = name
    )

    db.add(rol)
    db.commit()
