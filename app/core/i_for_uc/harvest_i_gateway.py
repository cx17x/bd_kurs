from abc import ABC, abstractmethod


class HarvestDBGatewayInterface(ABC):
    @abstractmethod
    async def update_quantity(self, harvest_code: int, new_quantity: int) -> None:
        """Обновить количество 'quantity'."""
        pass

    @abstractmethod
    async def create_harvest(self, harvest_code: int, harvest_type: str, quantity: int) -> None:
        """Создать новый 'Urozhai'."""
        pass
