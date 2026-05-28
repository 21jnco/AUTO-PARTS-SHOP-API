from fastapi import HTTPException, status

from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.models.customer import Customer

from sqlalchemy import select
from sqlalchemy.orm import Session


def create_customer(db: Session, customer_data: CustomerCreate) -> Customer:
    query_phone = select(Customer).where(Customer.phone == customer_data.phone)
    result_phone = db.execute(query_phone)

    customer_exists = result_phone.scalar_one_or_none()

    if customer_exists is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Customer with this phone already exists."
        )
    
    if customer_data.email is not None:
        query_email = select(Customer).where(Customer.email == customer_data.email)
        result_email = db.execute(query_email)

        customer_email = result_email.scalar_one_or_none()

        if customer_email is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Customer with this email already exists."
            )
    
    customer = Customer(
        name=customer_data.name,
        phone=customer_data.phone,
        email=customer_data.email
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def get_customer_by_id(db: Session, customer_id: int) -> Customer:
    query = select(Customer).where(Customer.id == customer_id)
    result = db.execute(query)

    customer = result.scalar_one_or_none()

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found."
        )
    
    return customer


def update_customer(db: Session, customer_id: int, customer_data: CustomerUpdate) -> Customer:
    query = select(Customer).where(Customer.id == customer_id)
    result = db.execute(query)

    customer = result.scalar_one_or_none()

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found."
        )
    
    if customer_data.phone is not None:
        query_phone = select(Customer).where(Customer.phone == customer_data.phone)
        result_phone = db.execute(query_phone)

        customer_phone = result_phone.scalar_one_or_none()

        if customer_phone is not None and customer_phone.id != customer_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Customer with this phone already exists."
            )
        
        customer.phone = customer_data.phone
    
    if customer_data.email is not None:
        query_email = select(Customer).where(Customer.email == customer_data.email)
        result_email = db.execute(query_email)

        customer_email = result_email.scalar_one_or_none()

        if customer_email is not None and customer_email.id != customer_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Customer with this email already exists."
            )
        
        customer.email = customer_data.email

    if customer_data.name is not None:
        customer.name = customer_data.name

    db.commit()
    db.refresh(customer)

    return customer


def get_all_customers(db: Session):
    query = select(Customer)
    result = db.execute(query)

    customers = result.scalars().all()
    
    return customers
