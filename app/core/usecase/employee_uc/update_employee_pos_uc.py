import dataclasses

from app.core.i_for_uc.employee_i_gateway import EmployeeDBGatewayInterface


@dataclasses.dataclass
class UpdateEmployeePositionDTO:
    employee_code: int
    new_position: str


class UpdateEmployeePositionUC:
    def __init__(self, employee_repo: EmployeeDBGatewayInterface):
        self.employee_repo = employee_repo

    async def execute(self, dto: UpdateEmployeePositionDTO) -> None:
        await self.employee_repo.update_employee_position(
            employee_code=dto.employee_code,
            new_position=dto.new_position
        )
