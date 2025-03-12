from pydantic import BaseModel

class roleBase(BaseModel):
    id: int
    name: str