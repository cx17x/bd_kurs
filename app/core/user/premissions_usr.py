def check_user_permissions(action: str) -> bool:
    """Проверка прав пользователя."""
    allowed_actions = ["view"]
    return action in allowed_actions
