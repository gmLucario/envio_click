from pydantic import BaseModel
from typing import List, Optional

from models.truck import TruckDetailsSchema


class WorkerSchema(BaseModel):
    fullname: str
    curp: str
    assigned_trucks: List[str] = []
    driving_truck: Optional[TruckDetailsSchema]

    class Config:
        schema_extra = {
            "example": {
                "curp": "MHJR760319KDFGSW45",
                "fullname": "John Doe",
                "assigned_trucks": ["12344986453", "12348940128"],
                "driving_truck": {
                    "truck_motor_serial": "36789213456",
                    "init_date": "2021-02-26T22:29:50Z",
                    "end_date": "2021-02-26T22:29:50Z",
                },
            }
        }


def get_obj_from_mongo(result: dict) -> WorkerSchema:
    result.pop("_id")
    return WorkerSchema(**result)
