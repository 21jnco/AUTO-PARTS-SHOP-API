from fastapi import APIRouter, status, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.services.product_service import (
    get_product_by_id,
    get_products_by_category_id,
    create_product,
    update_product,
    get_all_products
)

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/category_id/{category_id}", response_model=list[ProductResponse])
def get_product_by_category_id_endpoint(category_id: int, db: Session = Depends(get_db)):
    return get_products_by_category_id(db, category_id)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, product_id)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(product_data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product_data)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    
    return update_product(db, product_id, product_data)
