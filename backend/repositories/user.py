from contextlib import AbstractContextManager
from typing import List, Callable, Type, Optional

from sqlalchemy.orm import Session

from models import UsersModel, Parameters, Standards
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def get_all(self) -> list[Type[UsersModel]]:
        with self.session_factory() as session:
            return session.query(UsersModel).all()

    def get_user_by_id(self, user_id: int) -> UsersModel:
        with self.session_factory() as session:
            return session.query(UsersModel).filter(UsersModel.id==user_id).first()

    def get_user_by_email(self, email: str) -> UsersModel:
        with self.session_factory() as session:
            return session.query(UsersModel).filter(UsersModel.email==email).first()

    def insert(self, user: UsersModel) -> None:
        with self.session_factory() as session:
            session.add(user)
            session.commit()

    def get_all_used_email(self, email: str):
        with self.session_factory() as session:
            return session.query(UsersModel.email).all()

    def update_name(self, user_id: int, name: str) -> None:
        with self.session_factory() as session:
            session.query(UsersModel).filter(UsersModel.id == user_id).update({"name": name})
            session.commit()

    def update_height(self, user_id, height: int) -> None:
        with self.session_factory() as session:
            session.query(UsersModel).filter(UsersModel.id == user_id).update({"height": height})
            session.commit()

    def delete(self, user_id: int) -> None:
        with self.session_factory() as session:
            delete_user = session.query(UsersModel).filter(UsersModel.id==user_id).first()
            session.delete(delete_user)
            session.commit()

    def update_status_health_point(self, user_id, health_point_id: int) -> None:
        with self.session_factory() as session:
            session.query(UsersModel).filter(UsersModel.id == user_id).update({"point_id": health_point_id})
            session.commit()

    def update_parameters(self, user_id: int, **kwargs) -> None:
        with self.session_factory() as session:
            user = self.get_user_by_id(user_id=user_id)
            if user.parameters:
                for kw in kwargs:
                    if kwargs[kw] is not None:
                        setattr(user.parameters, kw, kwargs[kw])
            else:
                user.parameters = Parameters(**kwargs)
            session.add(user)
            session.commit()

    def update_standards(self, user_id: int, **kwargs):
        with self.session_factory() as session:
            user = self.get_user_by_id(user_id=user_id)
            if user.standards:
                for kw in kwargs:
                    if kwargs[kw] is not None:
                        setattr(user.standards, kw, kwargs[kw])
            else:
                user.standards = Standards(**kwargs)
            session.add(user)
            session.commit()
