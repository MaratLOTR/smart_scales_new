import random

from models import UsersModel, Parameters, Standards
from repositories import UserRepository
from schemas import AuthResponseSchemas
from web.controllers.BaseController import BaseController


class AuthenticationController(BaseController):
    '''Контроллер для аутентификации пользователя'''
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def __call__(self, email: str) -> AuthResponseSchemas:
        user = self.user_repository.get_user_by_email(email=email)
        if user is None:
            raise ValueError("Такого пользователя не существует")
        return AuthResponseSchemas(user_id=user.id)
