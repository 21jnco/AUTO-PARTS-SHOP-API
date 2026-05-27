from pydantic import BaseModel

from decimal import Decimal
from datetime import datetime

class ResponseOrder(BaseModel):
    status: str
    total_price: Decimal
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
