import enum
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class UsersModel(Base):
    """Таблица пользователей"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(Boolean)
    height = Column(Integer)
    email = Column(String, unique=True)

    standards_id = Column(Integer, ForeignKey('standards.id'), nullable=True)
    parameters_id = Column(Integer, ForeignKey('parameters.id'), nullable=True)
    point_id = Column(Integer, ForeignKey("status.point"), nullable=True)

    health_point = relationship("StatusModel", back_populates="user", lazy="subquery")
    parameters = relationship('Parameters', back_populates="user", lazy="subquery")
    standards = relationship("Standards", back_populates="user", lazy="subquery")
