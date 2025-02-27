from typing import Generator

from database.config import async_session
from crud.user import UserCRUD
from crud.accounts import AccountsCRUD
from crud.categories import CategoriesCRUD
from crud.transactions import TransactionCRUD


async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session


async def get_user_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield UserCRUD(session)

async def get_account_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield AccountsCRUD(session)

async def get_transaction_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield TransactionCRUD(session)

async def get_category_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield CategoriesCRUD(session)

