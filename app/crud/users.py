from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User
from typing import List


async def get_all_users(session: AsyncSession) -> List[User]:
    a = await session.scalars(select(User).order_by(User.id))
    return a.all()


async def create_user(session: AsyncSession, name: str) -> User:
    tmp = await session.scalar(select(User).where(User.name==name))
    if tmp:
        raise RuntimeError("User exists")
    u = User(name=name)
    session.add(u)
    await session.commit()
    return u