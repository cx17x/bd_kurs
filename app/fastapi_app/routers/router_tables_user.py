from fastapi import APIRouter, Depends, Request

from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter import SQLDBGetter
from app.fastapi_app.utils import render_template

router_tables_user = APIRouter()


@router_tables_user.get("/employee_table")
async def employee_table(request: Request, connection=Depends(get_db_connection), employee_code: int = None):
    gateway = SQLDBGetter(connection)
    if employee_code:
        employee = await gateway.get_by_id("Employee", "employee_code", employee_code)
        if not employee:
            return render_template('employees.html', error="Employee not found")
        return render_template('employees.html', employee=employee)
    else:
        employees = await gateway.get_all("Employee")
        return render_template('employees.html', employees=employees)


async def get_by_id(self, table_name, id_column, id_value):
    try:
        record = await self.connection.fetchrow(f'SELECT * FROM {table_name} WHERE {id_column} = $1', id_value)
        return dict(record) if record else None
    except Exception as e:
        print(f'Error fetching {table_name} with {id_column} = {id_value}: {e}')
        return None


@router_tables_user.get("/equipment_table")
async def equipment_table(request: Request, connection=Depends(get_db_connection), equipment_code: int = None):
    gateway = SQLDBGetter(connection)
    if equipment_code:
        equipment = await gateway.get_by_id("Equipment", "equipment_code", equipment_code)
        if not equipment:
            return render_template('equipment.html', error="Equipment not found")
        return render_template('equipment.html', equipment=equipment)
    else:
        equipment_list = await gateway.get_all("Equipment")
        return render_template('equipment.html', equipment_list=equipment_list)


@router_tables_user.get("/harvest_table")
async def harvest_table(request: Request, connection=Depends(get_db_connection), harvest_code: int = None):
    gateway = SQLDBGetter(connection)
    if harvest_code:
        harvest = await gateway.get_by_id("Harvest", "harvest_code", harvest_code)
        if not harvest:
            return render_template('harvest.html', error="Harvest not found")
        return render_template('harvest.html', harvest=harvest)
    else:
        harvests = await gateway.get_all("Harvest")
        return render_template('harvest.html', harvests=harvests)


@router_tables_user.get("/order_table")
async def order_table(request: Request, connection=Depends(get_db_connection), order_number: int = None):
    gateway = SQLDBGetter(connection)
    if order_number:
        order = await gateway.get_by_id("Orders", "order_number", order_number)
        if not order:
            return render_template('orders.html', error="Order not found")
        return render_template('orders.html', order=order)
    else:
        orders = await gateway.get_all("Orders")
        return render_template('orders.html', orders=orders)


@router_tables_user.get("/region_table")
async def region_table(request: Request, connection=Depends(get_db_connection), plot_code: int = None):
    gateway = SQLDBGetter(connection)
    if plot_code:
        region = await gateway.get_by_id("Region", "plot_code", plot_code)
        if not region:
            return render_template('regions.html', error="Region not found")
        return render_template('regions.html', region=region)
    else:
        regions = await gateway.get_all("Region")
        return render_template('regions.html', regions=regions)
