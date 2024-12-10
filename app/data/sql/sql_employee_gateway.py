import asyncpg
from asyncpg import Connection


class SQLEmployeeDBGateway:
    """Класс для выполнения операций с таблицей Employee."""

    def __init__(self, connection: Connection):
        self.connection = connection

    async def update_employee_position(self, employee_code: int, new_position: str) -> None:
        query = """
            UPDATE Employee
            SET position = $1
            WHERE employee_code = $2
        """
        await self.connection.execute(query, new_position, employee_code)

    async def update_employee_salary(self, employee_code: int, new_salary: float) -> None:
        query = """
            UPDATE Employee
            SET salary = $1
            WHERE employee_code = $2
        """
        await self.connection.execute(query, new_salary, employee_code)

    async def assign_employee_to_plot(self, employee_code: int, plot_code: int) -> None:
        query = """
            UPDATE Employee
            SET plot_code = $1
            WHERE employee_code = $2
        """
        await self.connection.execute(query, plot_code, employee_code)
