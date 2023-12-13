import random

from models import UsersModel, Parameters, Standards
from repositories import UserRepository
from web.controllers.BaseController import BaseController


class RegistrationNewUserController(BaseController):
    '''Контроллер для регистрации нового пользователя'''
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def __call__(self, name: str, email: str, sex: bool, height: int):
        tt = self._is_unique_email(email)
        if not self._is_unique_email(email=email):
            raise ValueError("Почта уже используется другим пользователем")
        user = UsersModel(name=name, email=email, sex=sex, height=height)
        return self.user_repository.insert(user=user)

    def _is_unique_email(self, email: str) -> bool:
        used_emails = self.user_repository.get_all_used_email(email)
        return (email,) not in used_emails
