from datetime import date

from pydantic import BaseModel

# User Schema


class Base(BaseModel):
    username:str


class Register(Base):
    password: str

class Password(Base):
    password:str

class Birthday(Base):
    birthday:str