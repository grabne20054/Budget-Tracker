from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from crud.transactions import TransactionCRUD
from crud.accounts import AccountsCRUD
from crud.user import UserCRUD
from crud.dependencies import get_transaction_crud, get_account_crud
from auth.action import get_current_user
import schemas.user as user_schema
import schemas.transaction as transaction_schema

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("")
async def create(
     transaction: transaction_schema.Base, current_user: user_schema.Base = Depends(get_current_user), db: TransactionCRUD = Depends(get_transaction_crud), account_db: AccountsCRUD = Depends(get_account_crud)
):
    account = await account_db.get_account_of_user(current_user.username)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    
    await db.create_transaction(transaction=transaction, accountId=account.id, account_db=account_db)
    return status.HTTP_201_CREATED

@router.get("")
async def get_transactions_by_account(
    current_user: user_schema.Base = Depends(get_current_user), db: TransactionCRUD = Depends(get_transaction_crud), account_db: AccountsCRUD = Depends(get_account_crud), limit: int = 5
):
    account = await account_db.get_account_of_user(current_user.username)
    transactions = await db.get_transactions_by_account(account_id=account.id, limit=limit)

    return transactions

@router.get("/category")
async def get_transactions_by_category_and_account(
    categoryId: int, current_user: user_schema.Base = Depends(get_current_user), db: TransactionCRUD = Depends(get_transaction_crud), account_db: AccountsCRUD = Depends(get_account_crud)
):
    account = await account_db.get_account_of_user(current_user.username)
    transactions = await db.get_transactions_by_category_and_account(category_id=categoryId, account_id=account.id)

    return transactions

@router.put("/paymentreason")
async def update_paymentreason(
    transactionId: int, paymentreason: str, db: TransactionCRUD = Depends(get_transaction_crud)
):
    await db.update_paymentreason(transaction_id=transactionId, paymentreason=paymentreason)
    return status.HTTP_200_OK


@router.put("/amount")
async def update_amount(
    transactionId: int, amount: float, db: TransactionCRUD = Depends(get_transaction_crud), account_db: AccountsCRUD = Depends(get_account_crud)
):
    await db.update_amount(transaction_id=transactionId, amount=amount, account_db=account_db)
    return status.HTTP_200_OK

@router.delete("")
async def delete(
    transactionId: int, db: TransactionCRUD = Depends(get_transaction_crud), account_db: AccountsCRUD = Depends(get_account_crud)
):
    transaction = await db.get_transaction_by_id(transactionId)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    await db.delete_transaction(transaction_id=transactionId, account_db=account_db)
    return status.HTTP_200_OK