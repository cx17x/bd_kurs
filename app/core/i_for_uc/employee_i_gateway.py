from abc import ABC, abstractmethod
from typing import List, Optional

from app.core.entites import Employee


class EmployeeDBGatewayInterface(ABC):
    """Интерфейс для работы с таблицей 'Employee'."""

    @abstractmethod
    async def update_employee_position(self, employee_code: int, new_position: str) -> None:
        """Обновить должность сотрудника по 'employee_code'."""
        pass

    @abstractmethod
    async def update_employee_salary(self, employee_code: int, new_salary: float) -> None:
        """Обновить зарплату сотрудника по 'employee_code'."""
        pass

    @abstractmethod
    async def assign_employee_to_plot(self, employee_code: int, plot_code: int) -> None:
        """Назначить сотрудника на участок."""
        pass
