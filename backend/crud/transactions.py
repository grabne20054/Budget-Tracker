from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from auth.utils import get_password_hash
from models.model import TransactionsModels
from crud.accounts import AccountsCRUD
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
    
    async def get_transactions_by_category_and_account(self, category_id: int, account_id: int):
        stmt = select(TransactionsModels).where(TransactionsModels.category_id == category_id, TransactionsModels.account_id == account_id)
        result = await self.db_session.execute(stmt)
        transactions = result.scalars().all()
        return transactions
    
    async def create_transaction(self, transaction: transaction_schema.Base, accountId: int, account_db: AccountsCRUD):
        transaction = TransactionsModels(
            paymentreason = transaction.paymentreason,
            amount=transaction.amount,
            account_id=accountId,
            category_id=transaction.category_id,
            finished=False,
            type=transaction.type
        )

        self.db_session.add(transaction)
        await account_db.update_balance(transaction)
        transaction.finished = True
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

    async def update_amount(self, transaction_id:int, amount:int, account_db: AccountsCRUD):
        stmt = (
            update(TransactionsModels)
            .where(TransactionsModels.id == transaction_id)
            .values(amount=amount)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

        transaction = await self.get_transaction_by_id(transaction_id)
        await account_db.update_balance(transaction)

        

    async def update_category(self, transaction_id:int, category_id: int):
        stmt = (
            update(TransactionsModels)
            .where(TransactionsModels.id == transaction_id)
            .values(category_id=category_id)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_transaction(self, transaction_id:int, account_db: AccountsCRUD):
        transaction = await self.get_transaction_by_id(transaction_id)
        if not transaction:
            return None
        else: 
            await account_db.revert_balance(transaction)
        stmt = delete(TransactionsModels).where(TransactionsModels.id == transaction_id)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def get_transaction_by_id(self, transaction_id:int):
        stmt = select(TransactionsModels).where(TransactionsModels.id == transaction_id)
        result = await self.db_session.execute(stmt)
        transaction = result.scalars().first()
        return transaction
