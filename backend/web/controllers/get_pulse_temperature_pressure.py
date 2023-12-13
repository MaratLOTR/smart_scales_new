import random
from typing import Optional

from models import Parameters, Standards
from models.base_recommendation_system import BaseRecommendationSystem
from repositories import UserRepository
from schemas import PulseTemperaturePressureStatusResponseModel
from schemas.pulse_temperature_pressure import PressureModel, StatusResponseModel
from utils.algorithm_calculating_status_health import algorithm_for_calculating_the_status_of_health
from utils.recommendation_system import RecommendationSystem
from utils.sqlalchemy_model_to_dict import asdict
from web.controllers.BaseController import BaseController


class GetPulseTemperaturePressureController(BaseController):
    def __init__(self, user_repository: UserRepository, recommendation_system: RecommendationSystem):
        self.user_repository = user_repository
        self.recommendation_system = recommendation_system

    def __call__(self, user_id: int) -> PulseTemperaturePressureStatusResponseModel:
        user = self.user_repository.get_user_by_id(user_id=user_id)

        if user is None:
            raise ValueError("Пользователь с таким ID отсутствует")

        self.recommendation_system.initialization_parameters_standards(standards=user.standards,
                                                                       parameters=user.parameters)

        try:
            pulse = self.recommendation_system.pulse()
            temperature = self.recommendation_system.temperature()
            systolic_pressure = self.recommendation_system.systolic_pressure()
            diastolic_pressure = self.recommendation_system.diastolic_pressure()
        except ValueError as msg:
            raise ValueError(str(msg))

        status_point = user.health_point.point if user.health_point else None
        status_description = user.health_point.message if user.health_point else None

        pressure = PressureModel(systolic_pressure=systolic_pressure, diastolic_pressure=diastolic_pressure)
        status = StatusResponseModel(health_point=status_point, description=status_description)

        return PulseTemperaturePressureStatusResponseModel(pulse=pulse, temperature=temperature, pressure=pressure,
                                                     status=status)
