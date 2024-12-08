import asyncpg

from app.core.i_for_uc.harvest_i_gateway import HarvestDBGatewayInterface


class SQLHarvestDBGateway(HarvestDBGatewayInterface):
    """Реализация интерфейса HarvestDBGatewayInterface."""

    def __init__(self, connection: asyncpg.Connection):
        self.connection = connection

    async def update_quantity(self, harvest_code: int, new_quantity: int) -> None:
        """Обновить количество 'quantity'."""
        query = """
            UPDATE Harvest
            SET quantity = $1
            WHERE harvest_code = $2
        """
        await self.connection.execute(query, new_quantity, harvest_code)

    async def create_harvest(self, harvest_code: int, harvest_type: str, quantity: int) -> None:
        """Создать новый 'Urozhai'."""
        query = """
            INSERT INTO Harvest (harvest_code, harvest_type, quantity)
            VALUES ($1, $2, $3)
        """
        await self.connection.execute(query, harvest_code, harvest_type, quantity)
