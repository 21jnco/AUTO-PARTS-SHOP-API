from pydantic import BaseModel

from decimal import Decimal
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    status: str
    total_price: Decimal
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
