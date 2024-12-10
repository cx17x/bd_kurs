import secrets

from fastapi import HTTPException, Depends, APIRouter, Request, Response
from fastapi.templating import Jinja2Templates

from app.core.entites import LoginData
from app.data.datebase import db
from app.fastapi_app.auth import admin_only, authenticate_user

login_m = APIRouter()

templates = Jinja2Templates(directory="templates")


@login_m.post("/login")
async def login(response: Response, login_data: LoginData):
    user = await db.get_user(login_data.username)
    if user and user.password == login_data.password:
        session_token = secrets.token_hex(16)
        await db.set_user_session_token(user.user_id, session_token)
        response.set_cookie(key="session_token", value=session_token, httponly=True)
        return {"user_id": user.user_id, "role": user.role}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@login_m.get("/admin", dependencies=[Depends(admin_only)])
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@login_m.get("/user", dependencies=[Depends(authenticate_user)])
async def user_page(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})
