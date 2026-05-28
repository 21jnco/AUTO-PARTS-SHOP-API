from fastapi import status, HTTPException

from app.schemas.product import ProductCreate, ProductUpdate
from app.models.product import Product
from app.models.category import Category

from sqlalchemy.orm import Session
from sqlalchemy import select


def create_product(db: Session, product_data: ProductCreate) -> Product:
    query_category = select(Category).where(Category.id == product_data.category_id)
    category = db.execute(query_category).scalar_one_or_none()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )
    
    if category.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category is not available."
        )

    product = Product(
        category_id=product_data.category_id,
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock_quantity=product_data.stock_quantity
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product_by_id(db: Session, product_id: int) -> Product:
    query = select(Product).where(Product.id == product_id)
    product = db.execute(query).scalar_one_or_none()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    return product

def get_all_products(db: Session) -> list[Product]:
    query = select(Product)
    products = db.execute(query).scalars().all()

    return products

def get_products_by_category_id(db: Session, category_id: int) -> list[Product]:
    query = select(Category).where(Category.id == category_id)
    category = db.execute(query).scalar_one_or_none()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    query_products = select(Product).where(Product.category_id == category_id)
    products = db.execute(query_products).scalars().all()

    return products


def update_product(db: Session, product_id: int, product_data: ProductUpdate) -> Product:
    query = select(Product).where(Product.id == product_id)
    product = db.execute(query).scalar_one_or_none()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    if product_data.description is not None:
        product.description = product_data.description

    product.name = product_data.name
    product.price = product_data.price
    product.stock_quantity = product_data.stock_quantity
    product.is_active = product_data.is_active

    db.commit()
    db.refresh(product)

    return product