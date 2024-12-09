
def check_admin_permissions(action: str) -> bool:
    """Проверка прав администратора."""
    allowed_actions = ["create", "update", "delete", "view"]
    return action in allowed_actions