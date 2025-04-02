from datetime import datetime

import enum
from sqlalchemy import Column, ForeignKey, Double, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship, backref
from typing import List
from uuid import uuid4

from database.config import Base



# Create User class
class UserModels(Base):
    __tablename__ = "users"
    username = Column(String(100), primary_key=True, unique=True)
    password =  Column(String(100))



class AccountsModels(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance =  Column(Double, default=0.0)

    username = Column(String(30), ForeignKey("users.username"), nullable=False, unique=True)
    user = relationship("UserModels", backref=backref("accountsmodels", uselist=False))


class CategoriesModels(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(30))
    description = Column(String(100))

    username = Column(String(30), ForeignKey("users.username"), nullable=False)
    user = relationship("UserModels", backref=backref("categoriesmodels", uselist=True))

    transactions = relationship("TransactionsModels")


class TransactionsModels(Base):
    __tablename__= "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    paymentreason = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.now())
    amount = Column(Integer, nullable=False)
    finished = Column(Boolean)
    type = Column(String(10), nullable=False)

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)