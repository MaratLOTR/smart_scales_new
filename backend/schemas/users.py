from pydantic import BaseModel


class UsersSchemas(BaseModel):
    id: int
    name: str
    sex: bool

    class Config:
        orm_mode = True
