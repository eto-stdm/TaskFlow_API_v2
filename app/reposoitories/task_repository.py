from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.models.tasks import Task


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all(self) -> list[Task]:
        query = select(Task).order_by(Task.id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int) -> Task | None:
        query = select(Task).where(Task.id == id)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_text(self, text: str) -> Task | None:
        query = select(Task).where(Task.text == text)
        result = await self.session.execute(query)
        return result.scalar()

    async def create(self, data: dict) -> Task:
        task = Task(**data)  # распаковка словаря
        self.session.add(task)
        try:
            await self.session.commit()
            await self.session.refresh(task)
        except:
            await self.session.rollback()
            raise
        return task

    async def update(self, task: Task, update_data: dict) -> Task | None:
        for key, value in update_data.items():
            setattr(task, key, value)
        try:
            await self.session.commit()
            await self.session.refresh(task)
        except:
            await self.session.rollback()
            raise
        return task

    async def delete(self, task: Task) -> None:
        try:
            await self.session.delete(task)
            await self.session.commit()
        except:
            await self.session.rollback()
            raise