import os

import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from app.data.datebase import db

from app.fastapi_app.common_router import main_router
from app.fastapi_app.routers.router_tables_user import router_tables_user
from app.fastapi_app.routers.routers_tables_admin import admin_router


def create_app() -> FastAPI:
    core_app = FastAPI()

    @core_app.on_event("startup")
    async def startup_event():
        await db.init_pool()

    @core_app.on_event("shutdown")
    async def shutdown_event():
        await db.close_pool()

    core_app.include_router(main_router)
    core_app.include_router(router_tables_user)
    core_app.include_router(admin_router)

    frontend_path = os.path.join(os.getcwd(), "templates")
    core_app.mount("/", StaticFiles(directory=frontend_path), name="static")

    frontend_path_user = os.path.join(os.getcwd(), "templates/user")
    core_app.mount("/", StaticFiles(directory=frontend_path_user), name="user_static")

    frontend_path_admin = os.path.join(os.getcwd(), "templates/admin")
    core_app.mount("/", StaticFiles(directory=frontend_path_admin), name="admin_static")

    return core_app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host='0.0.0.0', port=8000)
