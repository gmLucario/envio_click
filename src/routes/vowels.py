from fastapi import APIRouter

from models.response import GeneralResponse
from models.requests import VowelRequest

from handlers.section_a import get_vowels_summary


vowels_routers = APIRouter(
    prefix="/vowels",
    tags=["vowels"],
    responses={404: {"description": "Not found"}},
)

responses_info = {
    200: {
        "description": "success",
        "content": {
            "application/json": {
                "example": {
                    "data": {"vowels_count": 1, "new_line": "strong"},
                    "message": "success",
                    "code": 200,
                }
            }
        },
    }
}


@vowels_routers.post(
    "/",
    responses=responses_info,
    response_description="Change vowels and count them",
    status_code=200,
)
async def change_vowels(vowel_request: VowelRequest):
    return GeneralResponse(
        data=get_vowels_summary(vowel_request.line), message="success", code=200
    )
