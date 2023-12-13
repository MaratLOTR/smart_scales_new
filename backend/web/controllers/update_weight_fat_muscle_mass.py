import random
from typing import Optional

from models import UsersModel, Parameters, Standards
from repositories import UserRepository, ParametersRepository
from utils.sqlalchemy_model_to_dict import asdict
from web.controllers.BaseController import BaseController


class UpdateWeightFatMuscleMassController(BaseController):
    '''Контроллер для внесения в систему значений веса, жировой и мышечной массы'''
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def __call__(self, user_id: int, weight: Optional[int] = None, fat_mass: Optional[int] = None,
                 muscle_mass: Optional[int] = None):
        user = self.user_repository.get_user_by_id(user_id=user_id)

        if user is None:
            raise ValueError("Пользователь с таким ID отсутствует")

        if weight and fat_mass and muscle_mass:
            parameters = Parameters(weight=weight, fat_mass=fat_mass, muscle_mass=muscle_mass)
        else:
            parameters = self._generate_parameters(height=user.height)
        self.user_repository.update_parameters(user_id=user_id, **asdict(parameters))

        if not (user.standards and user.standards.weight and user.standards.fat_mass and user.standards.muscle_mass):
            standards = self._generate_standards(height=user.height, sex=user.sex)
            self.user_repository.update_standards(user_id=user_id, **asdict(standards))

        '''Старая версия алгоритма'''
        # if not user.parameters and (not weight or not fat_mass or not muscle_mass):
        #     parameters: Parameters = self._generate_parameters(height=user.height)
        # else:
        #     parameters = Parameters(weight=weight, fat_mass=fat_mass, muscle_mass=muscle_mass)
        # self.user_repository.update_parameters(user_id=user_id, **asdict(parameters))
        #
        # if not user.standards:
        #     standards = self._generate_standards(height=user.height, sex=user.sex)
        #     self.user_repository.update_standards(user_id=user_id, **asdict(standards))

    def _generate_standards(self, height: int, sex: bool) -> Standards:
        weight = height - random.randint(height-120, height-40)
        if sex:
            fat_mass = (height-100) * random.uniform(0.08,0.27)
        else:
            fat_mass = (height - 100) * random.uniform(0.15, 0.35)
        muscle_mass = random.randint(9200, 9700) / weight
        return Standards(weight=weight, fat_mass=fat_mass, muscle_mass=muscle_mass)

    def _generate_parameters(self, height: int) -> Parameters:
        weight = (height - 100) * random.uniform(a=0.6, b=1.1)
        fat_mass = weight*random.uniform(a=0.5, b=0.7)
        muscle_mass = weight - fat_mass
        return Parameters(weight=weight, fat_mass=fat_mass, muscle_mass=muscle_mass)
