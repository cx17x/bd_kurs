import dataclasses
from typing import Optional, List

from app.core.entites import HarvestType, Harvest
from app.core.i_for_uc.harvest_i_gateway import HarvestDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class UpdateQuantityDTO:
    harvest_code: int
    new_quantity: int


class UpdateQuantityUC(IUseCase):
    def __init__(self, harvest_repo: HarvestDBGatewayInterface):
        self.harvest_repo = harvest_repo

    async def execute(self, dto: UpdateQuantityDTO) -> None:
        await self.harvest_repo.update_quantity(harvest_code=dto.harvest_code, new_quantity=dto.new_quantity)
