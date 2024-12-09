from typing import Dict, List

from asyncpg import Connection
from fastapi import APIRouter, HTTPException, Depends

from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter.sql_db_getter import SQLDBGetter
from app.data.sql.sql_employee_gateway.sql_employee_gateway import SQLEmployeeDBGateway

employee_gateway = APIRouter()


@employee_gateway.put("/{employee_code}/position")
async def update_position(employee_code: int, new_position: str, connection: Connection = Depends(get_db_connection)):
    gateway = SQLEmployeeDBGateway(connection)
    try:
        await gateway.update_employee_position(employee_code, new_position)
        return {"message": "Position updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@employee_gateway.put("/{employee_code}/salary")
async def update_salary(employee_code: int, new_salary: float, connection: Connection = Depends(get_db_connection)):
    gateway = SQLEmployeeDBGateway(connection)
    try:
        await gateway.update_employee_salary(employee_code, new_salary)
        return {"message": "Salary updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@employee_gateway.put("/{employee_code}/plot")
async def assign_to_plot(employee_code: int, plot_code: int, connection: Connection = Depends(get_db_connection)):
    gateway = SQLEmployeeDBGateway(connection)
    try:
        await gateway.assign_employee_to_plot(employee_code, plot_code)
        return {"message": "Employee assigned to plot successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@employee_gateway.get("/")
async def get_all_employees(connection: Connection = Depends(get_db_connection)) -> List[Dict]:
    """Получить все записи из таблицы Employee."""
    gateway = SQLDBGetter(connection)
    return await gateway.get_all("Employee")


@employee_gateway.get("/{employee_code}")
async def get_employee_by_id(employee_code: int, connection: Connection = Depends(get_db_connection)) -> Dict:
    """Получить сотрудника по ID."""
    gateway = SQLDBGetter(connection)
    employee = await gateway.get_by_id("Employee", "employee_code", employee_code)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@employee_gateway.delete("/{employee_code}")
async def delete_employee_by_id(employee_code: int, connection: Connection = Depends(get_db_connection)):
    """Удалить сотрудника по ID."""
    gateway = SQLDBGetter(connection)
    await gateway.delete_by_id("Employee", "employee_code", employee_code)
    return {"message": "Employee deleted successfully"}
