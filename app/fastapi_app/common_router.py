from fastapi import APIRouter

from app.fastapi_app.routers.views_employee import employee_gateway
from app.fastapi_app.routers.views_equipment import equipment_gateway
from app.fastapi_app.routers.views_harvest import harvest_gateway
from app.fastapi_app.routers.views_order import order_gateway
from app.fastapi_app.routers.views_region import region_gateway

main_router = APIRouter()

main_router.include_router(
    employee_gateway,
    prefix='/employee'
)

main_router.include_router(
    equipment_gateway,
    prefix='/equipment'
)

main_router.include_router(
    harvest_gateway,
    prefix='/harvest'
)

main_router.include_router(
    order_gateway,
    prefix='/order'
)

main_router.include_router(
    region_gateway,
    prefix='/region'
)
