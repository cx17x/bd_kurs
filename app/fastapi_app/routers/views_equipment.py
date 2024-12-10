from typing import List, Dict, Optional

from asyncpg import Connection
from fastapi import Depends, HTTPException, APIRouter

from app.core.entites import EquipmentCondition
from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter import SQLDBGetter
from app.data.sql.sql_equipment_gateway import SQLEquipmentDBGateway

equipment_gateway = APIRouter()


@equipment_gateway.get("/")
async def get_all_equipment(connection: Connection = Depends(get_db_connection)) -> List[Dict]:
    """Получить все записи из таблицы Equipment."""
    gateway = SQLDBGetter(connection)
    return await gateway.get_all("Equipment")


@equipment_gateway.get("/{equipment_code}")
async def get_equipment_by_code(equipment_code: int, connection: Connection = Depends(get_db_connection)) -> Dict:
    """Получить оборудование по коду."""
    gateway = SQLDBGetter(connection)
    equipment = await gateway.get_by_id("Equipment", "equipment_code", equipment_code)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment


@equipment_gateway.delete("/{equipment_code}")
async def delete_equipment_by_code(equipment_code: int, connection: Connection = Depends(get_db_connection)):
    """Удалить оборудование по коду."""
    gateway = SQLDBGetter(connection)
    await gateway.delete_by_id("Equipment", "equipment_code", equipment_code)
    return {"message": "Equipment deleted successfully"}


@equipment_gateway.post("/create", status_code=201)
async def create_equipment(
        equipment_code: int,
        equipment_type: str,
        condition: EquipmentCondition,
        employee_code: Optional[int] = None,
        region_code: Optional[int] = None,
        connection: Connection = Depends(get_db_connection)
):
    """
    Создать новое оборудование.
    """
    gateway = SQLEquipmentDBGateway(connection)
    try:
        await gateway.create_equipment(equipment_code, equipment_type, condition, employee_code, region_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"status": "success", "message": "Equipment created successfully"}


@equipment_gateway.put("/update-condition", status_code=200)
async def update_equipment_condition(
        equipment_code: int,
        new_condition: EquipmentCondition,
        connection: Connection = Depends(get_db_connection)
):
    """
    Обновить состояние оборудования.
    """
    gateway = SQLEquipmentDBGateway(connection)
    try:
        await gateway.update_equipment_condition(equipment_code, new_condition)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"status": "success", "message": "Equipment condition updated successfully"}


@equipment_gateway.put("/assign-to-employee", status_code=200)
async def assign_equipment_to_employee(
        equipment_code: int,
        employee_code: int,
        connection: Connection = Depends(get_db_connection)
):
    """
    Назначить оборудование сотруднику.
    """
    gateway = SQLEquipmentDBGateway(connection)
    try:
        await gateway.assign_equipment_to_employee(equipment_code, employee_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"status": "success", "message": "Equipment assigned to employee successfully"}


@equipment_gateway.put("/assign-to-region", status_code=200)
async def assign_equipment_to_region(
        equipment_code: int,
        region_code: int,
        connection: Connection = Depends(get_db_connection)
):
    """
    Назначить оборудование региону.
    """
    gateway = SQLEquipmentDBGateway(connection)
    try:
        await gateway.assign_equipment_to_region(equipment_code, region_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"status": "success", "message": "Equipment assigned to region successfully"}
