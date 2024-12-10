from typing import Dict, List

from asyncpg import Connection
from fastapi import APIRouter, HTTPException, Depends


from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter import SQLDBGetter
from app.data.sql.sql_employee_gateway import SQLEmployeeDBGateway
from app.fastapi_app.auth import authenticate_user

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


@employee_gateway.get("/", dependencies=[Depends(authenticate_user)], response_model=List[Dict])
async def get_all_employees(connection: Session = Depends(get_db_connection)) -> List[Dict]:
    logger.info("Fetching all employees")
    gateway = SQLDBGetter(connection)
    employees = await gateway.get_all("Employee")
    if not employees:
        logger.warning("No employees found")
    return employees

@employee_gateway.get("/{employee_code}", dependencies=[Depends(authenticate_user)], response_model=Dict)
async def get_employee_by_id(employee_code: int, connection: Session = Depends(get_db_connection)) -> Dict:
    logger.info(f"Fetching employee with code {employee_code}")
    gateway = SQLDBGetter(connection)
    employee = await gateway.get_by_id("Employee", "employee_code", employee_code)
    if not employee:
        logger.warning(f"Employee with code {employee_code} not found")
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@employee_gateway.delete("/{employee_code}")
async def delete_employee_by_id(employee_code: int, connection: Connection = Depends(get_db_connection)):
    """Удалить сотрудника по ID."""
    gateway = SQLDBGetter(connection)
    await gateway.delete_by_id("Employee", "employee_code", employee_code)
    return {"message": "Employee deleted successfully"}
