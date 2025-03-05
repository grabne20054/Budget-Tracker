from pydantic import BaseModel

# Category Schema

class Base(BaseModel):
    name: str

class Register(Base):
    description: str
