from typing import AsyncGenerator

import asyncpg

from app.core.entites import User
from app.data.config import settings


class Database:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

        self.users = [
            User(1, "admin", "adminpass", "admin"),
            User(2, "123", "123", "user")
        ]
        self.tables = {
            1: "Table 1 data",
            2: "Table 2 data"
        }
        self.sessions = {}

    async def get_user(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return None

    async def init_pool(self):  # типо создание
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def close_pool(self):  # закрытие
        if self.pool:
            await self.pool.close()

    async def get_connection(self) -> AsyncGenerator[asyncpg.Connection, None]:
        """Асинхронный генератор для получения соединения."""
        if not self.pool:
            raise RuntimeError("Connection pool is not initialized. Call `init_pool` first.")
        async with self.pool.acquire() as connection:
            yield connection

    async def set_user_session_token(self, user_id, session_token):
        self.sessions[session_token] = user_id

    async def get_user_by_session_token(self, session_token):
        user_id = self.sessions.get(session_token)
        if user_id:
            return next((user for user in self.users if user.user_id == user_id), None)
        return None


db = Database(settings.DATABASE_URL)


async def get_db_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    async for connection in db.get_connection():
        yield connection
