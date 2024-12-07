from typing import Optional

import asyncpg

from app.core.entites import EquipmentCondition
from app.core.i_for_uc.equipment_i_gateway import EquipmentDBGatewayInterface


class SQLEquipmentDBGateway(EquipmentDBGatewayInterface):
    """Реализация интерфейса EquipmentDBGatewayInterface."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

    async def init_pool(self):
        """Инициализация пула соединений."""
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def create_equipment(self, equipment_code: int, equipment_type: str, condition: EquipmentCondition,
                               employee_code: Optional[int] = None, region_code: Optional[int] = None) -> None:
        """Создать новую запись 'Equipment'."""
        async with self.pool.acquire() as connection:
            query = """
                INSERT INTO Equipment (equipment_code, equipment_type, condition, employee_code, region_code)
                VALUES ($1, $2, $3, $4, $5)
            """
            await connection.execute(query, equipment_code, equipment_type, condition.value, employee_code, region_code)

    async def update_equipment_condition(self, equipment_code: int, new_condition: EquipmentCondition) -> None:
        """Обновить состояние оборудования 'EquipmentCondition'."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Equipment
                SET condition = $1
                WHERE equipment_code = $2
            """
            await connection.execute(query, new_condition.value, equipment_code)

    async def assign_equipment_to_employee(self, equipment_code: int, employee_code: int) -> None:
        """Назначить оборудование сотруднику."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Equipment
                SET employee_code = $1, region_code = NULL
                WHERE equipment_code = $2
            """
            await connection.execute(query, employee_code, equipment_code)

    async def assign_equipment_to_region(self, equipment_code: int, region_code: int) -> None:
        """Назначить оборудование региону."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Equipment
                SET region_code = $1, employee_code = NULL
                WHERE equipment_code = $2
            """
            await connection.execute(query, region_code, equipment_code)

    async def close(self):
        """Закрыть пул соединений."""
        if self.pool:
            await self.pool.close()
