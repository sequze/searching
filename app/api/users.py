from fastapi import APIRouter, Depends, HTTPException, status
from crud.users import get_all_users
from crud.users import create_user as create_user_db
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from typing import List
from core.schemas import UserRead


router = APIRouter(
    tags=["Users"]
)


@router.get("/", response_model=List[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    return await get_all_users(session)


@router.post("/", response_model=UserRead)
async def create_user(username: str, session: AsyncSession = Depends(db_helper.session_getter)):
    try:
        u = await create_user_db(session, username)
    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="user already exists")
    return u