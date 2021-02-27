from fastapi import APIRouter, Response
from models.truck import TruckSchema
from models.response import GeneralListResponse
from typing import List
from models.repository import ApiRepository

truck_routers = APIRouter(
    prefix="/trucks",
    tags=["trucks"],
    responses={404: {"description": "Not found"}},
)


repo = ApiRepository()


@truck_routers.post("/", response_description="Add multiple trucks", status_code=200)
async def add_trucks(trucks: List[TruckSchema], response: Response):
    repo.set_collection("trucks", index_fields=("motor_serial",))
    trucks_to_save = [
        truck
        for truck in trucks
        if not await repo.find_one({"motor_serial": truck.motor_serial})
    ]
    if not trucks_to_save:
        response.status_code = 400
        return GeneralListResponse(
            data=None, message="All the trucks have been inserted previously", code=400
        )

    await repo.insert_many(trucks_to_save)
    return GeneralListResponse(data=trucks_to_save, message="success", code=200)
