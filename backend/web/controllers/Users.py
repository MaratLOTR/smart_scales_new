from typing import List

from models import UsersModel
from repositories.base_repository import BaseRepository
from web.controllers.BaseController import BaseController


class UsersController(BaseController):
    def __init__(self, user_repository: BaseRepository):
        self.user_repository = user_repository

    def get_all_users(self) -> List[UsersModel]:
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id: int) -> UsersModel:
        user = self.user_repository.get_user_by_id(user_id=user_id)
        if user is not None:
            return user.parameters

    def insert_new_user(self, name: str, sex: bool, height: int, email: str):
        user = UsersModel(name=name, sex=sex, height=height, email=email)
        return self.user_repository.insert(user=user)
