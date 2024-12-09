import asyncpg

from app.core.entites import OrderStatus, Order, OrderCreateRequest
from app.core.i_for_uc.order_i_gateway import OrderDBGatewayInterface


class SQLOrderDBGateway(OrderDBGatewayInterface):
    """Реализация интерфейса OrderDBGatewayInterface."""

    def __init__(self, connection: asyncpg.Connection):
        self.connection = connection

    def to_entity(self, row: dict) -> Order:
        """Преобразовать строку результата запроса в объект Order."""
        # Преобразуем строку результата запроса в объект Order
        return Order(
            order_number=row['order_number'],
            status=OrderStatus(row['status']),
            order_date=row['order_date'],
            employee_code=row['employee_code']
        )

    def to_model(self, order_create_request: OrderCreateRequest) -> Order:
        """Преобразовать модель запроса в объект Order."""
        # Преобразуем данные запроса в объект модели Order
        return Order(
            order_number=order_create_request.order_number,
            status=order_create_request.status,
            order_date=order_create_request.order_date,
            employee_code=order_create_request.employee_code
        )

    async def create_order(self, order_number: int, status: OrderStatus, order_date: str, employee_code: int) -> None:
        """Создать новый заказ."""
        query = """
            INSERT INTO Orders (order_number, status, order_date, employee_code)
            VALUES ($1, $2, $3, $4)
        """
        await self.connection.execute(query, order_number, status.value, order_date, employee_code)

    async def update_order_status(self, order_number: int, new_status: OrderStatus) -> None:
        """Обновить статус заказа."""
        query = """
            UPDATE Orders
            SET status = $1
            WHERE order_number = $2
        """
        await self.connection.execute(query, new_status.value, order_number)
