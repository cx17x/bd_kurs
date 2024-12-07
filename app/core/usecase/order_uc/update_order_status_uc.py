import dataclasses

from app.core.entites import OrderStatus
from app.core.i_for_uc.order_i_gateway import OrderDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class UpdateOrderStatusDTO:
    order_number: int
    new_status: OrderStatus


class UpdateOrderStatusUC(IUseCase):
    def __init__(self, order_repo: OrderDBGatewayInterface):
        self.order_repo = order_repo

    async def execute(self, dto: UpdateOrderStatusDTO) -> None:
        """Execute the use case to update the status of an order."""
        await self.order_repo.update_order_status(
            order_number=dto.order_number,
            new_status=dto.new_status
        )