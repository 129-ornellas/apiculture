from pydantic import BaseModel

class GetForm(BaseModel):
    url: str
