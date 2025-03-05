from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from crud.categories import CategoriesCRUD
from crud.dependencies import get_category_crud
from auth.action import get_current_user
import schemas.user as user_schema
import schemas.categories as category_schema

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("")
async def create(
     category: category_schema.Register, current_user: user_schema.Base = Depends(get_current_user), db: CategoriesCRUD = Depends(get_category_crud)
):
    
    category = await db.create_category(category=category, username=current_user.username)

    return category

@router.get("")
async def get_categories(
    db: CategoriesCRUD = Depends(get_category_crud)
):
   categories = await db.get_categories()

   return categories

@router.put("/name")
async def update_name(
    new_name: str, categoryId: int, current_user: user_schema.Base = Depends(get_current_user), db: CategoriesCRUD = Depends(get_category_crud)
):
    return await db.update_category_name(category_id=categoryId, name=new_name, username=current_user.username)


@router.put("/description")
async def update_description(
    new_description: str, categoryId: int, current_user: user_schema.Base = Depends(get_current_user), db: CategoriesCRUD = Depends(get_category_crud)
):
    return await db.update_category_description(category_id=categoryId, description=new_description, username=current_user.username)
    

@router.delete("")
async def delete_category(
    categoryId: int, current_user: user_schema.Base = Depends(get_current_user), db: CategoriesCRUD = Depends(get_category_crud)
):
    return await db.delete_category(category_id=categoryId, username=current_user.username)

