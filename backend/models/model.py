from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from typing import List
from uuid import uuid4

from database.config import Base


# Create User class
class UserModels(Base):
    __tablename__ = "users"
    username = Column(String(30), primary_key=True, unique=True)
    password =  Column(String(30))

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False, unique=True)
    accounts = relationship("AccountsModels", backref=backref("usermodels", uselist=False))


class AccountsModels(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(30))
    balance =  Column(Integer)


class CategoriesModels(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(30))
    description = Column(String(100))

    transactions = relationship("TransactionsModels")


class TransactionsModels(Base):
    __tablename__= "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    paymentreason = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.now())
    amount = Column(Integer, nullable=False)

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)