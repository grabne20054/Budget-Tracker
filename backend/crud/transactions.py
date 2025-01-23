from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from auth.utils import get_password_hash
from models.model import TransactionsModels
import schemas.transaction as transaction_schema


class TransactionCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_transcations_by_account(self, account_id: int):
        stmt = select(TransactionsModels).where(TransactionsModels.account_id == account_id)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions
    
    async def get_transactions_by_category(self, category_id: int):
        stmt = select(TransactionsModels).where(TransactionsModels.category_id == category_id)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions
    
    async def create_transaction(self, transaction: transaction_schema.Base):
        transaction = TransactionsModels(
            paymentreason = transaction.paymentreason,
            created=transaction.created,
            amount=transaction.amount,
            account=transaction.account_id,
            category=transaction.category_id
        )

        self.db_session.add(TransactionsModels)
        await self.db_session.commit()
        return transaction

    async def update_paymentreason(self, transaction_id:int, paymentreason:str):
        stmt = (
            update(TransactionsModels)
            .where(TransactionsModels.id == transaction_id)
            .values(paymentreason=paymentreason)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_amount(self, transaction_id:int, amount:int):
        stmt = (
            update(TransactionsModels)
            .where(TransactionsModels.id == transaction_id)
            .values(amount=amount)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_category(self, transaction_id:int, category_id: int):
        stmt = (
            update(TransactionsModels)
            .where(TransactionsModels.id == transaction_id)
            .values(category_id=category_id)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_transaction(self, transaction_id:int):
        stmt = delete(TransactionsModels).where(TransactionsModels.id == transaction_id)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
