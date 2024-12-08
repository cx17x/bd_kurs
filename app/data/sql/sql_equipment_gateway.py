from typing import Optional

import asyncpg
from asyncpg import Connection

from app.core.entites import EquipmentCondition
from app.core.i_for_uc.equipment_i_gateway import EquipmentDBGatewayInterface


class SQLEquipmentDBGateway(EquipmentDBGatewayInterface):

    def __init__(self, connection: Connection):
        self.connection = connection

    async def create_equipment(
        self, equipment_code: int, equipment_type: str, condition: EquipmentCondition,
        employee_code: Optional[int] = None, region_code: Optional[int] = None
    ) -> None:

        query = """
            INSERT INTO Equipment (equipment_code, equipment_type, condition, employee_code, region_code)
            VALUES ($1, $2, $3, $4, $5)
        """
        await self.connection.execute(query, equipment_code, equipment_type, condition.value, employee_code, region_code)

    async def update_equipment_condition(self, equipment_code: int, new_condition: EquipmentCondition) -> None:
        query = """
            UPDATE Equipment
            SET condition = $1
            WHERE equipment_code = $2
        """
        await self.connection.execute(query, new_condition.value, equipment_code)

    async def assign_equipment_to_employee(self, equipment_code: int, employee_code: int) -> None:
        """Назначить оборудование сотруднику."""
        query = """
            UPDATE Equipment
            SET employee_code = $1, region_code = NULL
            WHERE equipment_code = $2
        """
        await self.connection.execute(query, employee_code, equipment_code)

    async def assign_equipment_to_region(self, equipment_code: int, region_code: int) -> None:
        """Назначить оборудование региону."""
        query = """
            UPDATE Equipment
            SET region_code = $1, employee_code = NULL
            WHERE equipment_code = $2
        """
        await self.connection.execute(query, region_code, equipment_code)