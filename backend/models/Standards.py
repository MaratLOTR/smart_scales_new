from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

from models.BaseClass import Base


class Standards(Base):
    __tablename__ = "standards"

    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    muscle_mass = Column(Integer)
    fat_mass = Column(Integer)
    pulse = Column(Integer)
    temperature = Column(Integer)
    systolic_pressure = Column(Integer)
    diastolic_pressure = Column(Integer)

    user = relationship('UsersModel', back_populates="standards", lazy="subquery")

