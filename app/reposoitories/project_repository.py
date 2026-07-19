from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.models.projects import Project


class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all(self) -> list[Project]:
        query = select(Project).order_by(Project.id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int) -> Project | None:
        query = select(Project).where(Project.id == id)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_name(self, name: str) -> Project | None:
        query = select(Project).where(Project.name == name)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_owner(self, owner_id: int) -> list[Project]:
        query = select(Project).where(Project.owner_id == owner_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, data: dict) -> Project:
        project = Project(**data)  # распаковка словаря
        self.session.add(project)
        try:
            await self.session.commit()
            await self.session.refresh(project)
        except:
            await self.session.rollback()
            raise
        return project

    async def update(self, project: Project, update_data: dict) -> Project | None:
        for key, value in update_data.items():
            setattr(project, key, value)
        try:
            await self.session.commit()
            await self.session.refresh(project)
        except:
            await self.session.rollback()
            raise
        return project

    async def delete(self) -> None:
        pass