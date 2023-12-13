from typing import Optional

from pydantic import BaseModel


class BaseRecommendationModel(BaseModel):
    user: Optional[int]
    standard: Optional[int]
    description: Optional[str]
