from fastapi import HTTPException, status

from app.models.customer import Customer
from app.models.order import Order
from app.models.product import Product
from app.models.order_item import OrderItem

from app.schemas.order import OrderCreate, OrderStatusUpdate

from sqlalchemy import select
from sqlalchemy.orm import Session

from decimal import Decimal


def create_order(db: Session, order_data: OrderCreate) -> Order:
    total_price = Decimal("0")

    query_customer = select(Customer).where(Customer.id == order_data.customer_id)
    customer = db.execute(query_customer).scalar_one_or_none()

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found."
        )
    
    if not order_data.items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order must contain at least one item."
        )
    
    order = Order(
        customer_id=customer.id,
        total_price=total_price
    )

    db.add(order)
    db.flush()

    for item in order_data.items:
        query_product = select(Product).where(Product.id == item.product_id)
        product = db.execute(query_product).scalar_one_or_none()

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found."
            )
        
        if product.is_active is False:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product is not available."
            )
        
        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Not enough product in stock."
            )
        
        subprice = product.price * item.quantity
        total_price += subprice

        product.stock_quantity -= item.quantity

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            price_at_moment=product.price
        )

        db.add(order_item)

    order.total_price = total_price

    db.commit()
    db.refresh(order)

    return order


def get_all_orders(db: Session) -> list[Order]:
    query = select(Order)
    orders = db.execute(query).scalars().all()
    
    return orders


def get_order_by_id(db: Session, order_id: int) -> Order:
    query = select(Order).where(Order.id == order_id)
    order = db.execute(query).scalar_one_or_none()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found."
        )
    
    return order


def update_order_status(db: Session, order_id: int, status_data: OrderStatusUpdate) -> Order:
    query = select(Order).where(Order.id == order_id)
    order = db.execute(query).scalar_one_or_none()

    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found."
        )
    
    order.status = status_data.status.value

    db.commit()
    db.refresh(order)

    return order
    