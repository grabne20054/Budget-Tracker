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

    async def get_account_of_user(self, username: str):
        stmt = select(AccountsModels).where(AccountsModels.username == username)
        result = await self.db_session.execute(stmt)
        account = result.scalars().all()
        return account

    async def create_account(self, account: account_schema.Base):
        account = AccountsModels(
            username=account.username,
            balance=0
        )

        self.db_session.add(account)
        await self.db_session.commit()
        return account

    async def update_balance(self, transaction: TransactionsModels):
        stmt = (
            update(AccountsModels)
            .where(AccountsModels.id == transaction.account_id)
            .values(balance=AccountsModels.balance + transaction.amount)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_account_of_user(self, username: str):
        account = self.get_account_of_user(username=username)

        stmt = delete(AccountsModels).where(AccountsModels.id == account.id)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
