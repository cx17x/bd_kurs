from typing import Dict, List, Optional

import asyncpg
from asyncpg import Connection
from app.core.i_for_uc.i_db_getter import BaseDBGetter


class SQLDBGetter(BaseDBGetter):
    def __init__(self, connection: Connection):
        self.connection = connection

    async def get_all(self, table_name: str) -> List[Dict]:
        """Получить все записи из таблицы."""
        query = f"SELECT * FROM {table_name}"
        rows = await self.connection.fetch(query)
        return [dict(row) for row in rows]

    async def get_by_id(self, table_name: str, id_column: str, record_id: int) -> Optional[Dict]:
        """Получить запись по ID."""
        query = f"SELECT * FROM {table_name} WHERE {id_column} = $1"
        row = await self.connection.fetchrow(query, record_id)
        return dict(row) if row else None

    async def delete_by_id(self, table_name: str, id_column: str, record_id: int) -> None:
        """Удалить запись по ID."""
        query = f"DELETE FROM {table_name} WHERE {id_column} = $1"
        await self.connection.execute(query, record_id)
