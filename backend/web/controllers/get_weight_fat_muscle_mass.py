from repositories import UserRepository
from schemas import PulseTemperaturePressureStatusResponseModel, WeightFatMuscleMassResponseModel
from utils.recommendation_system import RecommendationSystem
from web.controllers.BaseController import BaseController


class GetWeightFatMuscleMassController(BaseController):
    def __init__(self, user_repository: UserRepository, recommendation_system: RecommendationSystem):
        self.user_repository = user_repository
        self.recommendation_system = recommendation_system

    def __call__(self, user_id: int) -> WeightFatMuscleMassResponseModel:
        user = self.user_repository.get_user_by_id(user_id=user_id)

        if user is None:
            raise ValueError("Пользователь с таким ID отсутствует")

        self.recommendation_system.initialization_parameters_standards(standards=user.standards,
                                                                       parameters=user.parameters)

        try:
            weight = self.recommendation_system.weight()
            fat_mass = self.recommendation_system.fat_mass()
            muscle_mass = self.recommendation_system.muscle_mass()
        except ValueError as msg:
            raise ValueError(str(msg))

        return WeightFatMuscleMassResponseModel(weight=weight, fat_mass=fat_mass, muscle_mass=muscle_mass)
