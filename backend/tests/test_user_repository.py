import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DatabaseSettings

from repositories.user import UserRepository
from utils.database import Database

from models import UsersModel


@pytest.fixture()
def valid_user():
    return UsersModel(id=99, name="Marat", sex=True, height=182)


class TestUserRepository:
    db_set = DatabaseSettings()
    db = Database(db_url=db_set.get_connection_url())
    session_factory = db.session
    user_repository = UserRepository(session_factory=session_factory)

    def test_simple_get_query(self):
        users = self.user_repository.get_all()
        assert len(users) == 13
        assert isinstance(users[0], UsersModel)

    def test_insert_user(self, valid_user):
        count_records = len(self.user_repository.get_all())
        self.user_repository.insert(valid_user)
        assert count_records + 1 == len(self.user_repository.get_all())

    def test_get_user_by_id(self, valid_user):
        user = self.user_repository.get_user_by_id(user_id=99)
        assert user is not None
        assert user.name == valid_user.name
        assert user.sex == valid_user.sex
        assert user.height == valid_user.height

    def test_update_user_by_id(self):
        all_users = self.user_repository.get_all()
        count_records = len(all_users)
        updated_user_id = all_users[count_records - 1].id
        user = self.user_repository.get_user_by_id(user_id=updated_user_id)
        assert user is not None
        user_name = user.name
        new_user_name = "Alex" if user_name != "Alex" else "Marta"
        self.user_repository.update_name(user_id=user.id, name=new_user_name)

    def test_delete_user_by_id(self, valid_user):
        count_records = len(self.user_repository.get_all())
        deleted_user_id = valid_user.id
        self.user_repository.delete(user_id=deleted_user_id)
        deleted_user = self.user_repository.get_user_by_id(user_id=99)
        assert deleted_user is None
        assert count_records - 1 == len(self.user_repository.get_all())
