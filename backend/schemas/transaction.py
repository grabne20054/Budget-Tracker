from datetime import datetime

from pydantic import BaseModel
from typing import Literal

# User Schema


class Base(BaseModel):
    paymentreason: str
    amount: float
    type: Literal["expense", "income"]
    
    category_id: int

class UpdatePaymentReason(Base):
    paymentreason: str

class UpdateAmount(Base):
    amount: float

class UpdateCategory(Base):
    category_id: int



