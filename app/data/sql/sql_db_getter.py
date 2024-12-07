from typing import Dict, List, Optional

import asyncpg

from app.core.i_for_uc.i_db_getter import BaseDBGetter


class SQLDBGetter(BaseDBGetter):
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: Optional[asyncpg.Pool] = None

    async def init_pool(self):
        """Инициализировать пул соединений."""
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def get_all(self, table_name: str) -> List[Dict]:
        """Получить все записи из таблицы."""
        async with self.pool.acquire() as connection:
            query = f"SELECT * FROM {table_name}"
            rows = await connection.fetch(query)
            return [dict(row) for row in rows]

    async def get_by_id(self, table_name: str, id_column: str, record_id: int) -> Optional[Dict]:
        """Получить запись по ID."""
        async with self.pool.acquire() as connection:
            query = f"SELECT * FROM {table_name} WHERE {id_column} = $1"
            row = await connection.fetchrow(query, record_id)
            return dict(row) if row else None

    async def delete_by_id(self, table_name: str, id_column: str, record_id: int) -> None:
        """Удалить запись по ID."""
        async with self.pool.acquire() as connection:
            query = f"DELETE FROM {table_name} WHERE {id_column} = $1"
            await connection.execute(query, record_id)

    async def close(self):
        """Закрыть пул соединений."""
        if self.pool:
            await self.pool.close()
