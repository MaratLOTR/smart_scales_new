from pydantic import BaseModel

from schemas.base_recommendation import BaseRecommendationModel


class WeightFatMuscleMassResponseModel(BaseModel):
    weight: BaseRecommendationModel
    fat_mass: BaseRecommendationModel
    muscle_mass: BaseRecommendationModel
