from pydantic import BaseModel

class userBase(BaseModel):
    idUser: int | None = None
    firstName: str
    lastName: str
    role: int