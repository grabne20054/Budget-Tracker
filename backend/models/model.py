from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from typing import List
from uuid import uuid4

from database.config import Base


# Create User class
class UserModels(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname =  Column(String(30))
    lastname =  Column(String(30))
    password =  Column(String(30))

    accounts = relationship("AccountsModels")


class AccountsModels(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(30))
    balance =  Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    transactions = relationship("TransactionsModels")


class CategoriesModels(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(30))
    description = Column(String(100))

    transactions = relationship("TransactionsModels")


class TransactionsModels(Base):
    __tablename__= "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.now())
    amount = Column(Integer)

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)