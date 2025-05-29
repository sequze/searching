from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    # fields

class UserRead(UserBase):
    id: int