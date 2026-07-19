from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.models.attachments import Attachment


class AttachmentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_id(self, id: int) -> Attachment | None:
        query = select(Attachment).where(Attachment.id == id)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_task(self, task_id: int) -> list[Attachment]:
        query = select(Attachment).where(Attachment.task_id == task_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, data: dict) -> Attachment:
        attachment = Attachment(**data)  # распаковка словаря
        self.session.add(attachment)
        try:
            await self.session.commit()
            await self.session.refresh(attachment)
        except:
            await self.session.rollback()
            raise
        return attachment

    async def delete(self, attachment: Attachment) -> None:
        try:
            await self.session.delete(attachment)
            await self.session.commit()
        except:
            await self.session.rollback()
            raise