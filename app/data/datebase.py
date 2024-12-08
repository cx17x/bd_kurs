from typing import AsyncGenerator

import asyncpg
from app.data.config import settings


class Database:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

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


db = Database(settings.DATABASE_URL)
async def get_db_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    async for connection in db.get_connection():
        yield connection

