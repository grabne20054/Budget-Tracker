from datetime import datetime

from pydantic import BaseModel
from typing import Literal

# User Schema


class Base(BaseModel):
    paymentreason: str
    amount: int
    type: Literal["expense", "income"]
    
    category_id: int

class UpdatePaymentReason(Base):
    paymentreason: str

class UpdateAmount(Base):
    amount: int

class UpdateCategory(Base):
    category_id: int



