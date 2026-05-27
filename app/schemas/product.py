from pydantic import BaseModel

from datetime import datetime
from decimal import Decimal

class CreateProduct(BaseModel):
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    is_active: bool

class UpdateProduct(BaseModel):
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    is_active: bool

class ResponseProduct(BaseModel):
    id: int
    category_id: int
    name: str
    description: str
    price: Decimal
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }