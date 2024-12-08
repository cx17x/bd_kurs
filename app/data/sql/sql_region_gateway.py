from typing import Optional

import asyncpg

from app.core.entites import SoilType
from app.core.i_for_uc.region_i_gateway import RegionDBGatewayInterface


class SQLRegionDBGateway(RegionDBGatewayInterface):
    """Реализация интерфейса RegionDBGatewayInterface."""

    def __init__(self, connection: asyncpg.Connection):
        self.connection = connection

    async def update_region_description(self, plot_code: int, new_description: str) -> None:
        """Обновить описание региона по 'plot_code'."""
        query = """
            UPDATE Region
            SET plot_description = $1
            WHERE plot_code = $2
        """
        await self.connection.execute(query, new_description, plot_code)

    async def create_region(self, plot_code: int, soil_type: SoilType, plot_description: str,
                            harvest_code: Optional[int] = None) -> None:
        """Создать новый 'Region'."""
        query = """
            INSERT INTO Region (plot_code, soil_type, plot_description, harvest_code)
            VALUES ($1, $2, $3, $4)
        """
        await self.connection.execute(query, plot_code, soil_type.value, plot_description, harvest_code)
