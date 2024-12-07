from abc import abstractmethod, ABC


class RegionDBGatewayInterface(ABC):

    @abstractmethod
    async def update_region_description(self, region_code: int, new_description: str) -> None:
        """Обновить описание региона по 'region_code'."""
        pass

    @abstractmethod
    async def create_region(self, region_code: int, soil_type: str, description: str) -> None:
        """Создать новый 'Region'."""
        pass
