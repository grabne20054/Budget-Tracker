from datetime import datetime

from pydantic import BaseModel

# User Schema


class Base(BaseModel):
    paymentreason: str
    created: datetime
    amount: int

    account_id: int
    category_id: int

class UpdatePaymentReason(Base):
    paymentreason: str

class UpdateAmount(Base):
    amount: int

class UpdateCategory(Base):
    category_id: int



