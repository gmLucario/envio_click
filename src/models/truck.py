from pydantic import BaseModel, Field, validator
from datetime import datetime


class TruckSchema(BaseModel):
    motor_serial: str = Field(..., regex=r"^\d{11}$")
    branch: str

    class Config:
        schema_extra = {
            "example": {
                "motor_serial": "12904564320",
                "branch": "VW",
            }
        }


class TruckDetailsSchema(BaseModel):
    truck_motor_serial: str = Field(..., regex=r"^\d{11}$")
    init_date: datetime
    end_date: datetime

    @validator("end_date")
    def passwords_match(cls, v, values, **kwargs):
        if "init_date" in values and (v - values["init_date"]).days < 0:
            raise ValueError("end_date must be gratter than init_date")
        return v
