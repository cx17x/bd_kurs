import asyncpg

from app.core.i_for_uc.employee_i_gateway import EmployeeDBGatewayInterface


class SQLEmployeeDBGateway(EmployeeDBGatewayInterface):
    """Реализация интерфейса EmployeeDBGatewayInterface для работы с таблицей 'Employee'."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

    async def init_pool(self):
        """Инициализация пула соединений."""
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def update_employee_position(self, employee_code: int, new_position: str) -> None:
        """Обновить должность сотрудника по 'employee_code'."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Employee
                SET position = $1
                WHERE employee_code = $2
            """
            await connection.execute(query, new_position, employee_code)

    async def update_employee_salary(self, employee_code: int, new_salary: float) -> None:
        """Обновить зарплату сотрудника по 'employee_code'."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Employee
                SET salary = $1
                WHERE employee_code = $2
            """
            await connection.execute(query, new_salary, employee_code)

    async def assign_employee_to_plot(self, employee_code: int, plot_code: int) -> None:
        """Назначить сотрудника на участок."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Employee
                SET plot_code = $1
                WHERE employee_code = $2
            """
            await connection.execute(query, plot_code, employee_code)

    async def close(self):
        """Закрыть пул соединений."""
        if self.pool:
            await self.pool.close()
