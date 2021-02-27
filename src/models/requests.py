from pydantic import BaseModel


class VowelRequest(BaseModel):
    line: str
