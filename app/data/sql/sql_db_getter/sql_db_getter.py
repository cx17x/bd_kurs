from typing import Dict, List, Optional

from asyncpg import Connection
from app.core.i_for_uc.i_db_getter import BaseDBGetter
from app.core.user.premissions_adm import check_admin_permissions
from app.core.user.premissions_usr import check_user_permissions


class SQLDBGetter(BaseDBGetter):
    def __init__(self, connection: Connection, user_role: str):
        self.connection = connection
        self.user_role = user_role

    async def get_all(self, table_name: str) -> List[Dict]:
        """Получить все записи из таблицы."""
        if self.user_role == "admin":
            if not check_admin_permissions("view"):
                raise PermissionError("Admin does not have permission to view")
        elif self.user_role == "user":
            if not check_user_permissions("view"):
                raise PermissionError("User does not have permission to view")
        else:
            raise PermissionError("Unknown role")

        query = f"SELECT * FROM {table_name}"
        rows = await self.connection.fetch(query)
        return [dict(row) for row in rows]

    async def get_by_id(self, table_name: str, id_column: str, record_id: int) -> Optional[Dict]:
        """Получить запись по ID."""
        if self.user_role == "admin":
            if not check_admin_permissions("view"):
                raise PermissionError("Admin does not have permission to view")
        elif self.user_role == "user":
            if not check_user_permissions("view"):
                raise PermissionError("User does not have permission to view")
        else:
            raise PermissionError("Unknown role")
        query = f"SELECT * FROM {table_name} WHERE {id_column} = $1"
        row = await self.connection.fetchrow(query, record_id)
        return dict(row) if row else None

    async def delete_by_id(self, table_name: str, id_column: str, record_id: int) -> None:
        """Удалить запись по ID."""
        if self.user_role == "admin":
            if not check_admin_permissions("delete"):
                raise PermissionError("Admin does not have permission to delete")
        elif self.user_role == "user":
            raise PermissionError("User does not have permission to delete")  # Пользователь не может удалять записи
        else:
            raise PermissionError("Unknown role")

        query = f"DELETE FROM {table_name} WHERE {id_column} = $1"
        await self.connection.execute(query, record_id)
