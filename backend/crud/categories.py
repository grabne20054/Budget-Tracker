from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from auth.utils import get_password_hash
from models.model import CategoriesModels
import schemas.categories as categories_schema

class CategoriesCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_categories(self):
        stmt = select(CategoriesModels)
        result = await self.db_session.execute(stmt)
        categories = result.scalars().all()
        return categories
    
    async def create_category(self, category: categories_schema.Base):
        category = CategoriesModels(
            name=category.name,
            description=category.description
        )

        self.db_session.add(category)
        await self.db_session.commit()
        return category
    
    async def update_category_name(self,category_id: int, name:str ):
        stmt = (
            update(CategoriesModels)
            .where(CategoriesModels.id == category_id)
            .values(CategoriesModels.name == name)
            
        )
        
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)


    async def update_category_description(self, category_id: int, description: str):
        stmt = (
            update(CategoriesModels)
            .where(CategoriesModels.id == category_id)
            .values(CategoriesModels.description == description)
        )

        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_category(self, category_id):
        stmt = delete(CategoriesModels).where(CategoriesModels.id == category_id)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        