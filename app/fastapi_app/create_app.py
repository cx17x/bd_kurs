import os

import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from app.data.datebase import db

from app.fastapi_app.common_router import main_router


def create_app() -> FastAPI:
    core_app = FastAPI()

    @core_app.on_event("startup")
    async def startup_event():
        await db.init_pool()

    @core_app.on_event("shutdown")
    async def shutdown_event():
        await db.close_pool()

    core_app.include_router(main_router)
    frontend_path = os.path.join(os.getcwd(), "templates")
    core_app.mount("/", StaticFiles(directory=frontend_path), name="static")
    core_app.mount("/static", StaticFiles(directory="templates"), name="static")

    return core_app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host='0.0.0.0', port=8000)
