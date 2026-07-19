from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.models.users import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all(self) -> list[User]:
        query = select(User).order_by(User.id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int) -> User | None:
        query = select(User).where(User.id == id)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_username(self, username: str) -> User | None:
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar()

    async def create(self, data: dict) -> User:
        user = User(**data) # распаковка словаря
        self.session.add(user)
        try:
            await self.session.commit()
            await self.session.refresh(user)
        except:
            await self.session.rollback()
            raise
        return user

    async def update(self, user: User, update_data: dict) -> User | None:
        for key, value in update_data.items():
            setattr(user, key, value)
        try:
            await self.session.commit()
            await self.session.refresh(user)
        except:
            await self.session.rollback()
            raise
        return user

    async def delete(self, user: User) -> None:
        try:
            await self.session.delete(user)
            await self.session.commit()
        except:
            await self.session.rollback()
            raise