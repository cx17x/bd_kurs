import dataclasses

from app.core.entites import EquipmentCondition
from app.core.i_for_uc.equipment_i_gateway import EquipmentDBGatewayInterface


@dataclasses.dataclass
class UpdateEquipmentConditionDTO:
    equipment_code: int
    new_condition: EquipmentCondition


class UpdateEquipmentConditionUC:
    def __init__(self, equipment_repo: EquipmentDBGatewayInterface):
        self.equipment_repo = equipment_repo

    async def execute(self, dto: UpdateEquipmentConditionDTO) -> None:
        await self.equipment_repo.update_equipment_condition(
            equipment_code=dto.equipment_code,
            new_condition=dto.new_condition
        )
