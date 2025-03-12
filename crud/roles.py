from ..db.tables import Roles
from sqlalchemy.orm import Session
from ..schemas import roles_schemas

def createRol(name: str, db: Session):
    rol = Roles(
        roleName = name
    )

    db.add(rol)
    db.commit()
    return rol

def updateRol(rol: roles_schemas.roleBase, name: str, db: Session):
    rol.name = name
    db.commit
    return rol

def getRoles(db: Session):
    return db.query(Roles).all()

def getRolById(id: int, db: Session):
    return db.query(Roles).filter(Roles.idRole == id)

def getRolByName(name: str, db: Session):
    return db.query(Roles).filter(Roles.roleName == name)

def deleteRol(rol: roles_schemas, db: Session):
    db.delete(rol)
    db.commit()
    return rol