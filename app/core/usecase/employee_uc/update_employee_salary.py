import dataclasses

from app.core.i_for_uc.employee_i_gateway import EmployeeDBGatewayInterface


@dataclasses.dataclass
class UpdateEmployeeSalaryDTO:
    employee_code: int
    new_salary: float


class UpdateEmployeeSalaryUC:
    def __init__(self, employee_repo: EmployeeDBGatewayInterface):
        self.employee_repo = employee_repo

    async def execute(self, dto: UpdateEmployeeSalaryDTO) -> None:
        """Execute the use case to update the employee's salary."""
        await self.employee_repo.update_employee_salary(
            employee_code=dto.employee_code,
            new_salary=dto.new_salary
        )