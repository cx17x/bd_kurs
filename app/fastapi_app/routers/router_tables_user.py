from fastapi import APIRouter, Depends, Request

from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter import SQLDBGetter
from app.fastapi_app.utils import render_template

router_tables_user = APIRouter()


@router_tables_user.get("/employee_table")
async def employee_table(request: Request,
                         connection=Depends(get_db_connection),
                         employee_code: int = None,
                         sort: str = None,
                         action: str = None):
    gateway = SQLDBGetter(connection)

    # Проверяем, передан ли параметр employee_code в запросе
    if employee_code is not None:
        # Попытка найти сотрудника по его ID
        employee = await gateway.get_by_id("Employee", "employee_code", employee_code)
        if not employee:
            return render_template('employees.html', error="Employee not found")
        return render_template('employees.html', employee=employee)

    # Обработка действия "Show All Employees"
    if action == "show_all" or not employee_code:
        employees = await gateway.get_all("Employee")

    # Сортировка по столбцу
    if sort and employees:
        employees = sorted(employees, key=lambda x: x.get(sort, ""))

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
async def harvest_table(request: Request,
                        connection=Depends(get_db_connection),
                        harvest_code: int = None,
                        sort: str = None,
                        action: str = None):
    gateway = SQLDBGetter(connection)

    # Проверка параметра harvest_code: поиск конкретной записи
    if harvest_code is not None:
        harvest = await gateway.get_by_id("harvest", "harvest_code", harvest_code)
        if not harvest:
            return render_template('harvest.html', error="Harvest not found")
        return render_template('harvest.html', harvest=harvest)

    # Обработка действия "Show All Harvests"
    if action == "show_all" or not harvest_code:
        harvests = await gateway.get_all("harvest")
    else:
        harvests = []

    # Сортировка по столбцу, если параметр sort передан
    if sort and harvests:
        harvests = sorted(harvests, key=lambda x: x.get(sort, ""))

    # Возвращение данных в шаблон
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
