from pydantic import BaseModel

class roleBase(BaseModel):
    idRole: int
    roleName: str