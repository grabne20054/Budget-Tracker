from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.model import CategoriesModels
import schemas.categories as categories_schema

class CategoriesCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_categories(self) -> List[categories_schema.Base]:
        stmt = select(CategoriesModels)
        result = await self.db_session.execute(stmt)
        categories = result.scalars().all()
        return categories
    
    async def create_category(self, category: categories_schema.Register, username: str) -> categories_schema.Base:
        category = CategoriesModels(
            name=category.name,
            description=category.description,
            username=username
        )

        self.db_session.add(category)
        await self.db_session.commit()
        return category
    
    async def update_category_name(self,category_id: int, name:str, username:str):
        stmt = (
            update(CategoriesModels)
            .where(CategoriesModels.id == category_id)
            .where(CategoriesModels.username == username)
            .values(name=name)
        )
        
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)


    async def update_category_description(self, category_id: int, description: str, username: str):
        stmt = (
            update(CategoriesModels)
            .where(CategoriesModels.id == category_id)
            .where(CategoriesModels.username == username)
            .values(description=description)
        )

        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_category(self, category_id, username):
        stmt = delete(CategoriesModels).where(CategoriesModels.id == category_id).where(CategoriesModels.username == username)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        