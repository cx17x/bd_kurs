import dataclasses

from app.core.entites import OrderStatus
from app.core.i_for_uc.order_i_gateway import OrderDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class CreateOrderDTO:
    order_number: int
    status: OrderStatus
    order_date: str
    employee_code: int


class CreateOrderUC(IUseCase):
    def __init__(self, order_repo: OrderDBGatewayInterface):
        self.order_repo = order_repo

    async def execute(self, dto: CreateOrderDTO) -> None:
        """Execute the use case to create a new order."""
        await self.order_repo.create_order(
            order_number=dto.order_number,
            status=dto.status,
            order_date=dto.order_date,
            employee_code=dto.employee_code
        )
