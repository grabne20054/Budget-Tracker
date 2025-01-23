from datetime import date

from pydantic import BaseModel

# User Schema


class Base(BaseModel):
    username:str
    account_id: int


class Register(Base):
    password: str

