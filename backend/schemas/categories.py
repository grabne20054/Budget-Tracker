from pydantic import BaseModel

# Category Schema

class Base(BaseModel):
    name: str
    description:str

class UpdateName(Base):
    name:str

class UpdateDescription(Base):
    description:str