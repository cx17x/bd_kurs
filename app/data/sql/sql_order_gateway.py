import asyncpg

from app.core.entites import OrderStatus
from app.core.i_for_uc.order_i_gateway import OrderDBGatewayInterface


class SQLOrderDBGateway(OrderDBGatewayInterface):
    """Реализация интерфейса OrderDBGatewayInterface."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

    async def init_pool(self):
        """Инициализация пула соединений."""
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def create_order(self, order_number: int, status: OrderStatus, order_date: str, employee_code: int) -> None:
        """Создать новый заказ."""
        async with self.pool.acquire() as connection:
            query = """
                INSERT INTO Orders (order_number, status, order_date, employee_code)
                VALUES ($1, $2, $3, $4)
            """
            await connection.execute(query, order_number, status.value, order_date, employee_code)

    async def update_order_status(self, order_number: int, new_status: OrderStatus) -> None:
        """Обновить статус заказа."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Orders
                SET status = $1
                WHERE order_number = $2
            """
            await connection.execute(query, new_status.value, order_number)

    async def close(self):
        """Закрыть пул соединений."""
        if self.pool:
            await self.pool.close()
