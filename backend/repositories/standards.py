from typing import List, Callable, Type

from sqlalchemy.orm import Session

from models import Standards
from repositories.base_repository import BaseRepository


class StandardsRepository(BaseRepository):
    def __init__(self, session: Callable[[], Session]) -> None:
        self.session = session()

    def get_all(self) -> list[Type[Standards]]:
        return self.session.query(Standards).all()

    def get_standards_by_id(self, standards_id: int) -> Standards:
        return self.session.query(Standards).filter(Standards.id==standards_id).first()

    def insert(self, standards):
        self.session.add(standards)
        self.session.commit()
