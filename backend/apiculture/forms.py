from enum import Enum

from pydantic import BaseModel, HttpUrl


class RequestMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class RequestForm(BaseModel):
    url: HttpUrl
    method: RequestMethod
    params: dict | None = None
    headers: dict | None = None
