from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.model import AccountsModels, TransactionsModels
import schemas.accounts as account_schema



class AccountsCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_account_of_user(self, username: str) -> account_schema.Base:
        stmt = select(AccountsModels).where(AccountsModels.username == username)
        result = await self.db_session.execute(stmt)
        account = result.scalars().first()
        if account:
            account.balance = round(account.balance, 2)
        return account

    async def create_account(self, username: str):
        account = AccountsModels(
            username=username,
            balance=0.0
        )

        self.db_session.add(account)
        await self.db_session.commit()
        return account

    async def update_balance(self, transaction: TransactionsModels):
        if transaction.type == "expense":
            stmt = (
                update(AccountsModels)
                .where(AccountsModels.id == transaction.account_id)
                .values(balance=AccountsModels.balance - transaction.amount)
            )
        elif transaction.type == "income":
            stmt = (
                update(AccountsModels)
                .where(AccountsModels.id == transaction.account_id)
                .values(balance=AccountsModels.balance + transaction.amount)
            )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_account_of_user(self, username: str):
        account = await self.get_account_of_user(username=username)
        if not account:
            return None

        stmt = delete(AccountsModels).where(AccountsModels.username == account.username)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        return account
    
    async def revert_balance(self, transaction: TransactionsModels):
        if transaction.type == "expense":
            stmt = (
                update(AccountsModels)
                .where(AccountsModels.id == transaction.account_id)
                .values(balance=AccountsModels.balance + transaction.amount)
            )
        elif transaction.type == "income":
            stmt = (
                update(AccountsModels)
                .where(AccountsModels.id == transaction.account_id)
                .values(balance=AccountsModels.balance - transaction.amount)
            )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
