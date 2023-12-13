from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from models.BaseClass import Base


class Parameters(Base):
    """Таблица параметров человека"""

    __tablename__ = "parameters"

    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    muscle_mass = Column(Integer)
    fat_mass = Column(Integer)
    pulse = Column(Integer)
    temperature = Column(Integer)
    systolic_pressure = Column(Integer)
    diastolic_pressure = Column(Integer)

    user = relationship('UsersModel', back_populates="parameters", lazy="subquery")

    @hybrid_property
    def percent_fat(self):
        return round(self.fat_mass/self.weight, 2)

    @hybrid_property
    def percent_muscles(self):
        return round(self.muscle_mass / self.weight, 2)

    @hybrid_property
    def basal_metabolic_rate(self):
        return round((370 + (21.6 * self.muscle_mass)) * 1.1, 2)

    @hybrid_property
    def body_mass_index(self):
        return round(self.weight / self.height**2, 2)
