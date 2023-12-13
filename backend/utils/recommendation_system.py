from collections import namedtuple
from typing import Optional

from models import Standards, Parameters
from models.base_recommendation_system import BaseRecommendationSystem
from schemas.base_recommendation import BaseRecommendationModel

NORMAL_DEVIATION = 0.15

StatesDescriptions = namedtuple("StatesDescriptions", ["eq", "gt", "lt"])


class RecommendationSystem(BaseRecommendationSystem):
    def __init__(self):
        self.standards = None
        self.parameters = None

    def initialization_parameters_standards(self, standards: Standards, parameters: Parameters):
        self.standards = standards
        self.parameters = parameters

    def pulse(self) -> BaseRecommendationModel:
        return self._base_validate("pulse", StatesDescriptions(eq="Хороший пульс! :)",
                                                               lt="Слишком низкий пульс",
                                                               gt="Слишком высокий пульс"))

    def temperature(self) -> BaseRecommendationModel:
        return self._base_validate("temperature")

    def systolic_pressure(self) -> BaseRecommendationModel:
        return self._base_validate("systolic_pressure")

    def diastolic_pressure(self) -> BaseRecommendationModel:
        return self._base_validate("diastolic_pressure")

    def weight(self) -> BaseRecommendationModel:
        return self._base_validate("weight")

    def fat_mass(self) -> BaseRecommendationModel:
        return self._base_validate("fat_mass")

    def muscle_mass(self) -> BaseRecommendationModel:
        return self._base_validate("muscle_mass")

    def _base_validate(self, field: str, states_descriptions: Optional[StatesDescriptions] = None):
        try:
            user_value = getattr(self.parameters, field)
            standard_value = getattr(self.standards, field)
        except AttributeError as msg:
            return BaseRecommendationModel(user=None,
                                           standard=None,
                                           description=None)

        if user_value is None:
            raise ValueError(f"{field.capitalize()}: отсутствуют данные пользователя")
        if standard_value is None:
            raise ValueError(f"{field.capitalize()}: отсутствуют стандартные данные")

        delta_user_standard = user_value - standard_value
        normal_deviation_pulse = standard_value * NORMAL_DEVIATION
        if abs(delta_user_standard) <= normal_deviation_pulse:
            description = "Нормальное значение" if not states_descriptions else states_descriptions.eq
        elif delta_user_standard < 0:
            description = "Слишком никзое значение" if not states_descriptions else states_descriptions.lt
        else:
            description = "Слишком высокое значение" if not states_descriptions else states_descriptions.gt
        return BaseRecommendationModel(user=user_value,
                                       standard=standard_value,
                                       description=description)
