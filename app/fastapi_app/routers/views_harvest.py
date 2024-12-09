from typing import List, Dict

from asyncpg import Connection
from fastapi import APIRouter, HTTPException, Depends
from app.core.entites import HarvestType
from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter.sql_db_getter import SQLDBGetter
from app.data.sql.sql_harvest_gateway.sql_harvest_gateway import SQLHarvestDBGateway

harvest_gateway = APIRouter()


@harvest_gateway.get("/")
async def get_all_harvests(connection: Connection = Depends(get_db_connection)) -> List[Dict]:
    """Получить все записи из таблицы Harvest."""
    gateway = SQLDBGetter(connection)
    return await gateway.get_all("Harvest")


@harvest_gateway.get("/{harvest_code}")
async def get_harvest_by_code(harvest_code: int, connection: Connection = Depends(get_db_connection)) -> Dict:
    """Получить урожай по коду."""
    gateway = SQLDBGetter(connection)
    harvest = await gateway.get_by_id("Harvest", "harvest_code", harvest_code)
    if not harvest:
        raise HTTPException(status_code=404, detail="Harvest not found")
    return harvest


@harvest_gateway.delete("/{harvest_code}")
async def delete_harvest_by_code(harvest_code: int, connection: Connection = Depends(get_db_connection)):
    gateway = SQLDBGetter(connection)
    await gateway.delete_by_id("Harvest", "harvest_code", harvest_code)
    return {"message": "Harvest deleted successfully"}


@harvest_gateway.post("/create", status_code=201)
async def create_harvest(
        harvest_code: int,
        harvest_type: HarvestType,
        quantity: int,
        connection: Connection = Depends(get_db_connection)
):
    """
    Создать новый урожай.
    """
    gateway = SQLHarvestDBGateway(connection)
    try:
        await gateway.create_harvest(harvest_code, harvest_type.value, quantity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"status": "success", "message": "Harvest created successfully"}


@harvest_gateway.put("/update-quantity", status_code=200)
async def update_harvest_quantity(
        harvest_code: int,
        new_quantity: int,
        connection: Connection = Depends(get_db_connection)
):
    """
    Обновить количество урожая.
    """
    gateway = SQLHarvestDBGateway(connection)
    try:
        await gateway.update_quantity(harvest_code, new_quantity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"status": "success", "message": "Harvest quantity updated successfully"}
