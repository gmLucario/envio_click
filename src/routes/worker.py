from fastapi import APIRouter, Response
from typing import List
from models.worker import WorkerSchema, get_obj_from_mongo
from models.response import GeneralResponse
from models.repository import ApiRepository

workers_routers = APIRouter(
    prefix="/workers",
    tags=["workers"],
    responses={404: {"description": "Not found"}},
)


repo = ApiRepository()


@workers_routers.post(
    "/",
    response_description="Insert new worker",
    status_code=200,
)
async def add_worker(worker: WorkerSchema, response: Response):
    repo.set_collection("trucks", index_fields=("motor_serial",))
    worker.assigned_trucks = [
        ms for ms in worker.assigned_trucks if await repo.find_one({"motor_serial": ms})
    ]

    if (
        worker.driving_truck
        and worker.driving_truck.truck_motor_serial not in worker.assigned_trucks
    ):
        worker.driving_truck = None

    repo.set_collection("workers", index_fields=("curp",))
    data = await repo.update_or_insert(worker, {"curp": worker.curp})

    return GeneralResponse(
        data=get_obj_from_mongo(data),
        message="success",
        code=200,
    )
