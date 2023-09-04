from typing import Optional
from pydantic import BaseModel


class ResponseModel(BaseModel):
    data: Optional[dict] = None
    message: Optional[str] = None
