from sqlalchemy.orm import Session
from ..db.tables import User
from ..schemas import user_schemas

def createUser(data: user_schemas.userBase, db: Session):
    user = User(
        firstName = data.firstName,
        lastName = data.lastName,
        role = data.role
    )

    db.add(user)
    db.commit()
    return user

def updateUser(user: user_schemas.userBase, data: user_schemas.userBase, db: Session):
    user.firstName = data.firstName
    user.lastName = data.lastName
    user.role = data.role

    db.commit()
    return user

def getUser(db: Session):
    return db.query(User).all()

def getUserById(id: int, db: Session):
    return db.query(User).filter(User.idUser == id)

def getUserByFirstName(firtsName: str, db: Session):
    return db.query(User).filter(User.firstName == firtsName)

def deleteUser(user: user_schemas.userBase, db: Session):
    db.delete(user)
    db.commit()
    return user

