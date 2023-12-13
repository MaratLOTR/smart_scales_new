import random
from typing import Optional

from models import Parameters, Standards
from repositories import UserRepository
from utils.algorithm_calculating_status_health import algorithm_for_calculating_the_status_of_health
from utils.sqlalchemy_model_to_dict import asdict
from web.controllers.BaseController import BaseController


class UpdatePulseTemperaturePressureController(BaseController):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def __call__(self, user_id, pulse: Optional[int] = None, temperature: Optional[int] = None,
                 systolic_pressure: Optional[int] = None, diastolic_pressure: Optional[int] = None):
        user = self.user_repository.get_user_by_id(user_id=user_id)

        if user is None:
            raise ValueError("Пользователь с таким ID отсутствует")

        if pulse and temperature and systolic_pressure and diastolic_pressure:
            parameters = Parameters(pulse=pulse, temperature=temperature, systolic_pressure=systolic_pressure,
                                    diastolic_pressure=diastolic_pressure)
        else:
            parameters = self._generate_parameters()
        self.user_repository.update_parameters(user_id=user_id, **asdict(parameters))

        if not (user.standards.pulse and user.standards.temperature and user.standards.systolic_pressure
                and user.standards.diastolic_pressure):
            standards = self._generate_standards()
            self.user_repository.update_standards(user_id=user_id, **asdict(standards))

        health_point_id = algorithm_for_calculating_the_status_of_health()
        self.user_repository.update_status_health_point(user_id=user_id, health_point_id=health_point_id)


    def _generate_parameters(self) -> Parameters:
        pulse = random.randint(65, 110)
        temperature = random.uniform(35.5, 37.2)
        diastolic_pressure = random.randint(110, 140)
        systolic_pressure = random.randint(65, 100)
        parameter = Parameters(pulse=pulse, temperature=temperature, diastolic_pressure=diastolic_pressure,
                               systolic_pressure=systolic_pressure)
        return parameter

    def _generate_standards(self) -> Standards:
        pulse = random.randint(70, 100)
        temperature = random.uniform(36, 37)
        diastolic_pressure = random.randint(120, 130)
        systolic_pressure = random.randint(75, 90)
        standards = Standards(pulse=pulse, temperature=temperature, diastolic_pressure=diastolic_pressure,
                              systolic_pressure=systolic_pressure)
        return standards
