from pydantic import BaseModel

from datetime import datetime
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str
    category_id: int
    description: str | None = None
    price: Decimal
    stock_quantity: int

class ProductUpdate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    stock_quantity: int
    is_active: bool

class ProductResponse(BaseModel):
    id: int
    category_id: int
    name: str
    description: str | None = None
    price: Decimal
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }