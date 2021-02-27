from pydantic import BaseModel
from typing import Optional, List


class VowelSummary(BaseModel):
    vowels_count: int
    new_line: str


class GeneralResponse(BaseModel):
    data: Optional[BaseModel]
    message: str
    code: int = 200


class GeneralListResponse(BaseModel):
    data: Optional[List[BaseModel]]
    message: str
    code: int = 200
