from abc import ABC, abstractmethod

from app.core.entites import OrderStatus


class OrderDBGatewayInterface(ABC):
    @abstractmethod
    async def create_order(self, order_number: int, status: OrderStatus, order_date: str, employee_code: int) -> None:
        pass

    @abstractmethod
    async def update_order_status(self, order_number: int, new_status: OrderStatus) -> None:
        pass
