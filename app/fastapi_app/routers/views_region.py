from typing import List

import asyncpg
from fastapi import Depends, HTTPException, APIRouter

from app.core.entites import Region
from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter.sql_db_getter import SQLDBGetter
from app.data.sql.sql_region_gateway.sql_region_gateway import SQLRegionDBGateway

region_gateway = APIRouter()


@region_gateway.get("/", response_model=List[Region])
async def get_all_regions(connection: asyncpg.Connection = Depends(get_db_connection)) -> List[Region]:
    """Получить все регионы."""
    gateway = SQLDBGetter(connection)
    regions = await gateway.get_all("Region")  # Получить все регионы
    return [Region(**region) for region in regions]  # Преобразовать записи в датаклассы Region


@region_gateway.get("/{plot_code}", response_model=Region)
async def get_region_by_plot_code(plot_code: int,
                                  connection: asyncpg.Connection = Depends(get_db_connection)) -> Region:
    """Получить регион по plot_code."""
    gateway = SQLDBGetter(connection)
    region = await gateway.get_by_id("Region", "plot_code", plot_code)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return Region(**region)


@region_gateway.post("/create", status_code=201)
async def create_region(region_request: Region, connection: asyncpg.Connection = Depends(get_db_connection)):
    """Создать новый регион."""
    gateway = SQLRegionDBGateway(connection)
    try:
        await gateway.create_region(
            region_request.plot_code,
            region_request.soil_type,
            region_request.plot_description,
            region_request.harvest_code
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating region: {str(e)}")
    return {"status": "success", "message": "Region created successfully"}


@region_gateway.put("/update-description", status_code=200)
async def update_region_description(
        plot_code: int,
        new_description: str,
        connection: asyncpg.Connection = Depends(get_db_connection)
):
    """Обновить описание региона по plot_code."""
    gateway = SQLRegionDBGateway(connection)
    try:
        await gateway.update_region_description(plot_code, new_description)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating region description: {str(e)}")
    return {"status": "success", "message": "Region description updated successfully"}


@region_gateway.delete("/{plot_code}", status_code=200)
async def delete_region(plot_code: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    """Удалить регион по plot_code."""
    gateway = SQLDBGetter(connection)
    try:
        await gateway.delete_by_id("Region", "plot_code", plot_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting region: {str(e)}")
    return {"status": "success", "message": "Region deleted successfully"}
