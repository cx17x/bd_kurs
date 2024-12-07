import dataclasses

from app.core.i_for_uc.region_i_gateway import RegionDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class CreateRegionDTO:
    region_code: int
    soil_type: str
    description: str


class CreateRegionUC(IUseCase):
    def __init__(self, region_repo: RegionDBGatewayInterface):
        self.region_repo = region_repo

    async def execute(self, dto: CreateRegionDTO) -> None:
        await self.region_repo.create_region(
         region_code=dto.region_code, soil_type=dto.soil_type, description=dto.description
        )
