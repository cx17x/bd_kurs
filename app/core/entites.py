import dataclasses
from enum import Enum
from typing import Optional


class HarvestType(Enum):
    WHEAT = 'PSHENICA'
    CORN = 'KUKURUZA'
    OATS = 'OVES'


class SoilType(Enum):
    CHERNOZEM = 'CHERNOZEM'
    SANDY = 'PESCHANAYA'
    LOAMY = 'SUPESCHANAYA'


class EquipmentCondition(Enum):
    OPERATIONAL = 'ISPRAVNO'
    NON_OPERATIONAL = 'NEISPRAVNO'
    UNDER_REPAIR = 'REMONT'


class OrderStatus(Enum):
    IN_PROGRESS = 'V_RABOTE'
    COMPLETED = 'ZAVERSHEN'
    POSTPONED = 'OTLOZHEN'


@dataclasses.dataclass
class Harvest:  # Harvest
    harvest_code: int
    harvest_type: HarvestType
    quantity: int


@dataclasses.dataclass
class Region:  # Region (Field)
    plot_code: int
    soil_type: SoilType
    plot_description: str
    harvest_code: Optional[int] = None


@dataclasses.dataclass
class Equipment:  # Equipment
    equipment_code: int
    equipment_type: str
    condition: EquipmentCondition
    employee_code: Optional[int] = None
    region_code: Optional[int] = None


@dataclasses.dataclass
class Order:  # Order
    order_number: int
    status: OrderStatus
    order_date: str  # ISO8601 format (YYYY-MM-DD)
    employee_code: int


@dataclasses.dataclass
class Employee:  # Employee
    employee_code: int
    full_name: str
    position: str
    salary: float
    plot_code: Optional[int] = None
