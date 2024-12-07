from abc import ABC, abstractmethod
from typing import Optional

from app.core.entites import EquipmentCondition


class EquipmentDBGatewayInterface(ABC):
    @abstractmethod
    async def create_equipment(self, equipment_code: int, equipment_type: str, condition: EquipmentCondition,
                               employee_code: Optional[int] = None, region_code: Optional[int] = None) -> None:
        """Создать новую запись 'Equipment'."""
        pass

    @abstractmethod
    async def update_equipment_condition(self, equipment_code: int, new_condition: EquipmentCondition) -> None:
        """Обновить состояние оборудования 'EquipmentCondition'."""
        pass

    @abstractmethod
    async def assign_equipment_to_employee(self, equipment_code: int, employee_code: int) -> None:
        """Назначить оборудование сотруднику."""
        pass

    @abstractmethod
    async def assign_equipment_to_region(self, equipment_code: int, region_code: int) -> None:
        """Назначить оборудование региону."""
        pass
