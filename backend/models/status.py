import enum
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class StatusModel(Base):
    """Таблица общего состояния пользователя"""
    __tablename__ = "status"

    point = Column(Integer, primary_key=True)
    message = Column(String)

    user = relationship('UsersModel', back_populates="health_point", lazy="subquery")

