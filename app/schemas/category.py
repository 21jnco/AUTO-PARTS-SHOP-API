from pydantic import BaseModel

from datetime import datetime

class CreateCategory(BaseModel):
    name: str
    desctiption: str

class UpdateCategory(BaseModel):
    name: str
    description: str

class ResponseCategory(BaseModel):
    id: int
    name: str
    description: str
    is_active: bool
    created_at = datetime
    updated_at = datetime

    model_config = {
        "from_attributes": True
    }
