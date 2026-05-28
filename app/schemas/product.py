from pydantic import BaseModel, Field

from datetime import datetime
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=255)
    category_id: int
    description: str | None = None
    price: Decimal = Field(gt=0)
    stock_quantity: int = Field(ge=0)

class ProductUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=255)
    description: str | None = None
    price: Decimal = Field(gt=0)
    stock_quantity: int = Field(ge=0)
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