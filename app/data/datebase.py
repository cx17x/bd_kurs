import asyncpg
from contextlib import asynccontextmanager
from app.data.config import settings  # предполагается, что настройки хранятся в settings.py


@asynccontextmanager
async def get_db_connection():
    conn = await asyncpg.connect(settings.DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()


print(get_db_connection)
