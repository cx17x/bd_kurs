import asyncpg
from fastapi import APIRouter, Depends, Request, HTTPException

from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter import SQLDBGetter
from app.fastapi_app.utils import render_template_adm

admin_router = APIRouter()


@admin_router.get("/admin/employee_table")
async def employee_table(request: Request, connection=Depends(get_db_connection), employee_code: int = None):
    gateway = SQLDBGetter(connection)
    if employee_code:
        employee = await gateway.get_by_id("Employee", "employee_code", employee_code)
        if not employee:
            return render_template_adm('employees.html', error="Employee not found")
        return render_template_adm('employees.html', employee=employee)
    else:
        employees = await gateway.get_all("Employee")
        return render_template_adm('employees.html', employees=employees)


@admin_router.delete("/admin/employee/{employee_code}", status_code=200)
async def delete_employee(employee_code: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    gateway = SQLDBGetter(connection)

    # Проверяем, существует ли запись с указанным employee_code
    existing_employee = await gateway.get_by_id("Employee", "employee_code", employee_code)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    try:
        await gateway.delete_by_id("Employee", "employee_code", employee_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting employee: {str(e)}")

    return {"status": "success", "message": "Employee deleted successfully"}


@admin_router.get("/admin/equipment_table")
async def equipment_table(request: Request, connection=Depends(get_db_connection), equipment_code: int = None):
    gateway = SQLDBGetter(connection)
    if equipment_code:
        equipment = await gateway.get_by_id("Equipment", "equipment_code", equipment_code)
        if not equipment:
            return render_template_adm('equipment.html', error="Equipment not found")
        return render_template_adm('equipment.html', equipment=equipment)
    else:
        equipment_list = await gateway.get_all("Equipment")
        return render_template_adm('equipment.html', equipment_list=equipment_list)


@admin_router.delete("/admin/equipment/{equipment_code}", status_code=200)
async def delete_equipment(equipment_code: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    gateway = SQLDBGetter(connection)

    # Проверяем, существует ли запись с указанным equipment_code
    existing_equipment = await gateway.get_by_id("Equipment", "equipment_code", equipment_code)
    if not existing_equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")

    try:
        await gateway.delete_by_id("Equipment", "equipment_code", equipment_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting equipment: {str(e)}")

    return {"status": "success", "message": "Equipment deleted successfully"}


@admin_router.get("/admin/harvest_table")
async def harvest_table(request: Request, connection=Depends(get_db_connection), harvest_code: int = None):
    gateway = SQLDBGetter(connection)
    if harvest_code:
        harvest = await gateway.get_by_id("Harvest", "harvest_code", harvest_code)
        if not harvest:
            return render_template_adm('harvest.html', error="Harvest not found")
        return render_template_adm('harvest.html', harvest=harvest)
    else:
        harvests = await gateway.get_all("Harvest")
        return render_template_adm('harvest.html', harvests=harvests)


@admin_router.delete("/admin/harvest/{harvest_code}", status_code=200)
async def delete_harvest(harvest_code: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    gateway = SQLDBGetter(connection)

    # Проверяем, существует ли запись с указанным harvest_code
    existing_harvest = await gateway.get_by_id("Harvest", "harvest_code", harvest_code)
    if not existing_harvest:
        raise HTTPException(status_code=404, detail="Harvest not found")

    try:
        await gateway.delete_by_id("Harvest", "harvest_code", harvest_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting harvest: {str(e)}")

    return {"status": "success", "message": "Harvest deleted successfully"}


@admin_router.get("/admin/order_table")
async def order_table(request: Request, connection=Depends(get_db_connection), order_number: int = None):
    gateway = SQLDBGetter(connection)
    if order_number:
        order = await gateway.get_by_id("Orders", "order_number", order_number)
        if not order:
            return render_template_adm('orders.html', error="Order not found")
        return render_template_adm('orders.html', order=order)
    else:
        orders = await gateway.get_all("Orders")
        return render_template_adm('orders.html', orders=orders)


@admin_router.delete("/admin/order/{order_number}", status_code=200)
async def delete_order(order_number: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    gateway = SQLDBGetter(connection)

    # Проверяем, существует ли запись с указанным order_number
    existing_order = await gateway.get_by_id("Orders", "order_number", order_number)
    if not existing_order:
        raise HTTPException(status_code=404, detail="Order not found")

    try:
        await gateway.delete_by_id("Orders", "order_number", order_number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting order: {str(e)}")

    return {"status": "success", "message": "Order deleted successfully"}


@admin_router.get("/admin/region_table")
async def region_table(request: Request, connection=Depends(get_db_connection), plot_code: int = None):
    gateway = SQLDBGetter(connection)
    if plot_code:
        region = await gateway.get_by_id("Region", "plot_code", plot_code)
        if not region:
            return render_template_adm('regions.html', error="Region not found")
        return render_template_adm('regions.html', region=region)
    else:
        regions = await gateway.get_all("Region")
        return render_template_adm('regions.html', regions=regions)


@admin_router.delete("/admin/region/{plot_code}", status_code=200)
async def delete_region(plot_code: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    gateway = SQLDBGetter(connection)
    try:
        await gateway.delete_by_id("Region", "plot_code", plot_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting region: {str(e)}")
    return {"status": "success", "message": "Region deleted successfully"}

# @admin_router.post("/admin/region/create", status_code=201)
# async def create_region(region_request: Region, connection: asyncpg.Connection = Depends(get_db_connection)):
#     """Создать новый регион."""
#     gateway = SQLRegionDBGateway(connection)
#     try:
#         await gateway.create_region(
#             region_request.plot_code,
#             region_request.soil_type,
#             region_request.plot_description,
#             region_request.harvest_code
#         )
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Error creating region: {str(e)}")
#     return {"status": "success", "message": "Region created successfully"}
