from enum import Enum

from pydantic import BaseModel, HttpUrl


class RequestMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"

class RequestForm(BaseModel):
    url: HttpUrl
    method: RequestMethod
    body: dict | None = None
    accept: str
