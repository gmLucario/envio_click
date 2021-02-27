from pydantic import BaseModel
from pymongo import ASCENDING
from typing import List
from dotenv import load_dotenv
import os
import motor.motor_asyncio


load_dotenv()


def _make_url(db_config: dict):
    url = db_config.get("type")
    url += f'://{db_config.get("user")}'
    url += f':{db_config.get("password")}'
    url += f'@{db_config.get("host")}'
    url += f':{db_config.get("port")}'

    return url


class ApiRepository:
    """
    Methods that interact with the db
    """

    def __init__(self):
        client = motor.motor_asyncio.AsyncIOMotorClient(
            _make_url(
                db_config={
                    "type": os.getenv("DB_TYPE"),
                    "host": os.getenv("MONGO_HOST"),
                    "user": os.getenv("MONGO_USER"),
                    "password": os.getenv("MONGO_PASSWORD"),
                    "port": os.getenv("MONGO_PORT"),
                    "db": os.getenv("DB_NAME"),
                }
            )
        )

        self._db = client[os.getenv("DB_NAME")]

    def set_collection(self, collection: str, index_fields: tuple = ()) -> None:
        self._collection = self._db[collection]
        self._collection.create_index(
            [(index, ASCENDING) for index in index_fields], unique=True
        )

    def find_one(self, filters: dict) -> bool:
        return self._collection.find_one(filters)

    def update_or_insert(self, obj_to_save: BaseModel, filters: dict):
        return self._collection.find_one_and_update(
            filters, {"$set": obj_to_save.dict()}, upsert=True, return_document=True
        )

    def insert_many_trucks(self, list_objs: List[BaseModel]):
        return self._collection.insert_many([o.dict() for o in list_objs])
