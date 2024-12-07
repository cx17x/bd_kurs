from abc import ABC, abstractmethod
from typing import List, Optional, Dict


class BaseDBGetter(ABC):

    @abstractmethod
    async def get_all(self, table_name: str) -> List[Dict]:
        """Получить все записи из таблицы."""
        pass

    @abstractmethod
    async def get_by_id(self, table_name: str, id_column: str, record_id: int) -> Optional[Dict]:
        """Получить запись по ID."""
        pass

    @abstractmethod
    async def delete_by_id(self, table_name: str, id_column: str, record_id: int) -> None:
        """Удалить запись по ID."""
        pass
