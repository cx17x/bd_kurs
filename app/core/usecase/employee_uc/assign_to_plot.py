import dataclasses

from app.core.i_for_uc.employee_i_gateway import EmployeeDBGatewayInterface


@dataclasses.dataclass
class AssignEmployeeToPlotDTO:
    employee_code: int
    plot_code: int


class AssignEmployeeToPlotUC:
    def __init__(self, employee_repo: EmployeeDBGatewayInterface):
        self.employee_repo = employee_repo

    async def execute(self, dto: AssignEmployeeToPlotDTO) -> None:
        """Execute the use case to assign an employee to a plot."""
        await self.employee_repo.assign_employee_to_plot(
            employee_code=dto.employee_code,
            plot_code=dto.plot_code
        )
