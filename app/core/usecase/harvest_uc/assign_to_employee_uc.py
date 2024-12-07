import dataclasses

from app.core.i_for_uc.equipment_i_gateway import EquipmentDBGatewayInterface


@dataclasses.dataclass
class AssignEquipmentToEmployeeDTO:
    equipment_code: int
    employee_code: int


class AssignEquipmentToEmployeeUC:
    def __init__(self, equipment_repo: EquipmentDBGatewayInterface):
        self.equipment_repo = equipment_repo

    async def execute(self, dto: AssignEquipmentToEmployeeDTO) -> None:
        await self.equipment_repo.assign_equipment_to_employee(
            equipment_code=dto.equipment_code,
            employee_code=dto.employee_code
        )
