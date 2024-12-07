import dataclasses

from app.core.i_for_uc.equipment_i_gateway import EquipmentDBGatewayInterface


@dataclasses.dataclass
class AssignEquipmentToRegionDTO:
    equipment_code: int
    region_code: int


class AssignEquipmentToRegionUC:
    def __init__(self, equipment_repo: EquipmentDBGatewayInterface):
        self.equipment_repo = equipment_repo

    async def execute(self, dto: AssignEquipmentToRegionDTO) -> None:
        """Execute the use case to assign equipment to a region."""
        await self.equipment_repo.assign_equipment_to_region(
            equipment_code=dto.equipment_code,
            region_code=dto.region_code
        )