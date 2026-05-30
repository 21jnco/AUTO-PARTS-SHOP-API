from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.order import (
    OrderCreate,
    OrderStatusUpdate,
    OrderResponse
)

from app.services.order_service import (
    get_order_by_id,
    create_order,
    update_order_status,
    get_all_orders
)


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_id(db, order_id)


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order_endpoint(
    order_data: OrderCreate,
    db: Session = Depends(get_db)
):
    return create_order(db, order_data)


@router.put("/{order_id}", response_model=OrderResponse)
def update_order_status_endpoint(
    order_id: int,
    order_data: OrderStatusUpdate,
    db: Session = Depends(get_db)
):
    return update_order_status(db, order_id, order_data)