import dataclasses
from typing import Optional

from app.core.entites import EquipmentCondition
from app.core.i_for_uc.equipment_i_gateway import EquipmentDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class CreateEquipmentDTO:
    equipment_code: int
    equipment_type: str
    condition: EquipmentCondition
    employee_code: Optional[int] = None
    region_code: Optional[int] = None


class CreateEquipmentUC(IUseCase):
    def __init__(self, equipment_repo: EquipmentDBGatewayInterface):
        self.equipment_repo = equipment_repo

    async def execute(self, dto: CreateEquipmentDTO) -> None:
        await self.equipment_repo.create_equipment(
            equipment_code=dto.equipment_code,
            equipment_type=dto.equipment_type,
            condition=dto.condition,
            employee_code=dto.employee_code,
            region_code=dto.region_code
        )