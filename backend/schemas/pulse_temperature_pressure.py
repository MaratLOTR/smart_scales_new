from typing import Optional

from pydantic import BaseModel
from schemas.base_recommendation import BaseRecommendationModel


class PressureModel(BaseModel):
    systolic_pressure: BaseRecommendationModel
    diastolic_pressure: BaseRecommendationModel


class StatusResponseModel(BaseModel):
    health_point: Optional[int]
    description: Optional[str]


class PulseTemperaturePressureStatusResponseModel(BaseModel):
    pressure: PressureModel
    pulse: BaseRecommendationModel
    temperature: BaseRecommendationModel
    status: StatusResponseModel
