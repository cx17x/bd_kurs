import dataclasses

from app.core.i_for_uc.harvest_i_gateway import HarvestDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class CreateHarvestDTO:
    harvest_code: int
    harvest_type: str
    quantity: int


class CreateHarvestUC(IUseCase):
    def __init__(self, harvest_repo: HarvestDBGatewayInterface):
        self.harvest_repo = harvest_repo

    async def execute(self, dto: CreateHarvestDTO) -> None:
        await self.harvest_repo.create_harvest(harvest_code=dto.harvest_code, harvest_type=dto.harvest_type,
                                               quantity=dto.quantity)
