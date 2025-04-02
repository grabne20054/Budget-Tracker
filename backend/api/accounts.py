from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from crud.accounts import AccountsCRUD
from crud.user import UserCRUD
from crud.dependencies import get_account_crud
from auth.action import get_current_user
import schemas.accounts as account_schema
import schemas.user as user_schema
import schemas.transaction as transaction_schema

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("")
async def create(
    current_user: user_schema.Base = Depends(get_current_user), db: AccountsCRUD = Depends(get_account_crud)
) -> account_schema.Base:
    if await db.get_account_of_user(username=current_user.username):
        raise HTTPException(status_code=400, detail="Only one account possible per user")
    else:
        account = await db.create_account(username=current_user.username)
        return account


@router.delete("")
async def delete(
    current_user: user_schema.Base = Depends(get_current_user), db: AccountsCRUD = Depends(get_account_crud)
):
    if await db.delete_account_of_user(username=current_user.username) == None:
        raise HTTPException(status_code=404, detail="Account not found")
    return status.HTTP_200_OK


@router.get("")
async def get_account(
    current_user: user_schema.Base = Depends(get_current_user), db: AccountsCRUD = Depends(get_account_crud)
) -> account_schema.Base:
    account = await db.get_account_of_user(username=current_user.username)

    return account
