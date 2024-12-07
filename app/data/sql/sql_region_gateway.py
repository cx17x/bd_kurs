import asyncpg

from app.core.i_for_uc.region_i_gateway import RegionDBGatewayInterface


class SQLRegionDBGateway(RegionDBGatewayInterface):
    """Реализация интерфейса RegionDBGatewayInterface."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.pool: asyncpg.Pool = None

    async def init_pool(self):
        """Инициализация пула соединений."""
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.database_url)

    async def update_region_description(self, region_code: int, new_description: str) -> None:
        """Обновить описание региона по 'region_code'."""
        async with self.pool.acquire() as connection:
            query = """
                UPDATE Region
                SET description = $1
                WHERE region_code = $2
            """
            await connection.execute(query, new_description, region_code)

    async def create_region(self, region_code: int, soil_type: str, description: str) -> None:
        """Создать новый 'Region'."""
        async with self.pool.acquire() as connection:
            query = """
                INSERT INTO Region (region_code, soil_type, description)
                VALUES ($1, $2, $3)
            """
            await connection.execute(query, region_code, soil_type, description)

    async def close(self):
        """Закрыть пул соединений."""
        if self.pool:
            await self.pool.close()