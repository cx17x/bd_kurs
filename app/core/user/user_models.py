from dataclasses import dataclass
from typing import Optional


class UserBase:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class UserCreate(UserBase):
    """Модель для создания пользователя"""
    pass


class UserInDB(UserBase):
    """Модель для пользователя в базе данных (с сохраненным паролем)"""

    def __init__(self, username: str, hashed_password: str):
        super().__init__(username, None)  # Пароль не передается напрямую
        self.hashed_password = hashed_password


class AdminBase(UserBase):
    """Модель для администратора"""

    def __init__(self, username: str, password: str, admin_key: str):
        super().__init__(username, password)
        self.admin_key = admin_key


class AdminInDB(AdminBase):
    """Модель для администратора в базе данных"""

    def __init__(self, username: str, hashed_password: str, hashed_admin_key: str):
        super().__init__(username, None, None)  # Пароль и ключ не передаются напрямую
        self.hashed_password = hashed_password
        self.hashed_admin_key = hashed_admin_key
