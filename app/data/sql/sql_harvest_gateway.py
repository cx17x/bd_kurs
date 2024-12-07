import asyncpg

from app.core.i_for_uc.harvest_i_gateway import HarvestDBGatewayInterface


class SQLHarvestDBGateway(HarvestDBGatewayInterface):
    """Реализация интерфейса HarvestDBGatewayInterface."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

    async def init_pool(self):
        """Инициализация пула соединений."""
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def update_quantity(self, harvest_code: int, new_quantity: int) -> None:
        """Обновить количество 'quantity'."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Harvest
                SET quantity = $1
                WHERE harvest_code = $2
            """
            await connection.execute(query, new_quantity, harvest_code)

    async def create_harvest(self, harvest_code: int, harvest_type: str, quantity: int) -> None:
        """Создать новый 'Urozhai'."""
        async with self.pool.acquire() as connection:
            query = """
                INSERT INTO Harvest (harvest_code, harvest_type, quantity)
                VALUES ($1, $2, $3)
            """
            await connection.execute(query, harvest_code, harvest_type, quantity)

    async def close(self):
        """Закрыть пул соединений."""
        if self.pool:
            await self.pool.close()
