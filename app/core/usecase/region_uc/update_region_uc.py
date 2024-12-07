import dataclasses

from app.core.i_for_uc.region_i_gateway import RegionDBGatewayInterface
from app.core.usecase import IUseCase


@dataclasses.dataclass
class UpdateRegionDescriptionDTO:
    region_code: int
    new_description: str

class UpdateRegionDescriptionUC(IUseCase):
    def __init__(self, region_repo: RegionDBGatewayInterface):
        self.region_repo = region_repo

    async def execute(self, dto: UpdateRegionDescriptionDTO) -> None:
        """Execute the use case to update the description of a region."""
        await self.region_repo.update_region_description(
            region_code=dto.region_code, new_description=dto.new_description
        )