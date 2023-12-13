from pydantic import BaseModel


class AuthResponseSchemas(BaseModel):
    user_id: int

    class Config:
        orm_mode = True
