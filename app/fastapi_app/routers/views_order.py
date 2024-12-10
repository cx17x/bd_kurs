import asyncpg
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict

from app.core.entites import OrderStatus, OrderCreateRequest
from app.data.datebase import get_db_connection
from app.data.sql.sql_db_getter import SQLDBGetter
from app.data.sql.sql_order_gateway import SQLOrderDBGateway

order_gateway = APIRouter()


@order_gateway.get("/", response_model=List[Dict])
async def get_all_orders(connection: asyncpg.Connection = Depends(get_db_connection)) -> List[Dict]:
    """Получить все заказы."""
    gateway = SQLDBGetter(connection)
    try:
        return await gateway.get_all("Orders")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching orders: {str(e)}")


@order_gateway.get("/{order_number}", response_model=Dict)
async def get_order_by_number(order_number: int, connection: asyncpg.Connection = Depends(get_db_connection)) -> Dict:
    """Получить заказ по номеру заказа."""
    gateway = SQLOrderDBGateway(connection)
    order = await gateway.get_by_id("Orders", "order_number", order_number)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# @order_gateway.delete("/admin/order/{order_number}", status_code=200)
# async def delete_order(order_number: int, connection: asyncpg.Connection = Depends(get_db_connection)):
#     gateway = SQLDBGetter(connection)
#
#     # Проверяем, существует ли запись с указанным order_number
#     existing_order = await gateway.get_by_id("Orders", "order_number", order_number)
#     if not existing_order:
#         raise HTTPException(status_code=404, detail="Order not found")
#
#     try:
#         await gateway.delete_by_id("Orders", "order_number", order_number)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Error deleting order: {str(e)}")
#
#     return {"status": "success", "message": "Order deleted successfully"}
#

@order_gateway.post("/create", status_code=201)
async def create_order(
        order_request: OrderCreateRequest,
        connection: asyncpg.Connection = Depends(get_db_connection)
):
    """Создать новый заказ."""
    gateway = SQLOrderDBGateway(connection)
    try:
        await gateway.create_order(
            order_request.order_number,
            order_request.status,
            order_request.order_date,
            order_request.employee_code
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating order: {str(e)}")
    return {"status": "success", "message": "Order created successfully"}


@order_gateway.put("/update-status", status_code=200)
async def update_order_status(
        order_number: int,
        new_status: OrderStatus,
        connection: asyncpg.Connection = Depends(get_db_connection)
):
    """Обновить статус заказа."""
    gateway = SQLOrderDBGateway(connection)
    try:
        await gateway.update_order_status(order_number, new_status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating order status: {str(e)}")
    return {"status": "success", "message": "Order status updated successfully"}


# Delete order by order_number
@order_gateway.delete("/{order_number}")
async def delete_order_by_number(order_number: int, connection: asyncpg.Connection = Depends(get_db_connection)):
    """Удалить заказ по номеру заказа."""
    gateway = SQLDBGetter(connection)
    try:
        await gateway.delete_by_id("Orders", "order_number", order_number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting order: {str(e)}")
    return {"status": "success", "message": "Order deleted successfully"}
