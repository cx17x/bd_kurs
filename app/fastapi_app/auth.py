from fastapi import HTTPException, Depends, Request

from app.core.entites import User
from app.data.datebase import db


async def get_current_user(request: Request):
    session_token = request.cookies.get("session_token")
    if not session_token:
        return None
    user = await db.get_user_by_session_token(session_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")
    return user


async def authenticate_user(user: User = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


async def admin_only(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user
