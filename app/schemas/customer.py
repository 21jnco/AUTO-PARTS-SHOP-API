from pydantic import BaseModel

from datetime import datetime

class CustomerCreate(BaseModel):
    name: str
    phone: str
    email: str | None = None

class CustomerUpdate(BaseModel):
    name: str
    phone: str
    email: str | None = None

class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }