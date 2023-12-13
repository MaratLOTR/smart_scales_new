from contextlib import AbstractContextManager
from typing import Callable, Type, Optional

from sqlalchemy.orm import Session

from models import Parameters
from repositories.base_repository import BaseRepository


class ParametersRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> list[Type[Parameters]]:
        with self.session_factory() as session:
            return session.query(Parameters).all()

    def get_by_id(self, parameter_id: int) -> Parameters:
        with self.session_factory() as session:
            return session.query(Parameters).filter(Parameters.id == parameter_id).first()

    def insert_new_parameter(self, parameter):
        with self.session_factory() as session:
            session.add(parameter)
            session.commit()

    def update_health_parameter(self, user_id, pulse: Optional[int] = None, temperature: Optional[int] = None,
                                systolic_pressure: Optional[int] = None, diastolic_pressure: Optional[int] = None):
        with self.session_factory() as session:
            paramater: Parameters = session.query(Parameters).filter(Parameters.user.id == user_id)
            if pulse:
                paramater.pulse = pulse
            if temperature:
                paramater.temperature = paramater
            if diastolic_pressure:
                paramater.diastolic_pressure = diastolic_pressure
            if systolic_pressure:
                paramater.systolic_pressure = systolic_pressure
            session.commit()

    def update_weight_fat_muscle_mass(self, user_id, weight: Optional[int] = None, muscle_mass: Optional[int] = None,
                               fat_mass: Optional[int] = None):
        with self.session_factory() as session:
            paramater_record: Parameters = session.query(Parameters).filter(Parameters.user.id == user_id)
            parameter = paramater_record if paramater_record else Parameters()
            if weight:
                parameter.weight = weight
            if muscle_mass:
                parameter.muscle_mass = muscle_mass
            if fat_mass:
                parameter.fat_mass = fat_mass
            session.commit()

