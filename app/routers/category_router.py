from fastapi import APIRouter, Depends, status

from app.database import get_db

from sqlalchemy.orm import Session

from app.services.category_service import(
    get_category_by_id,
    create_category,
    update_category,
    get_all_categories
)

from app.schemas.category import(
    CategoryResponse,
    CategoryCreate,
    CategoryUpdate
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return get_category_by_id(db, category_id)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category_endpoint(category_data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category_data)


@router.put("/{categoty_id}", response_model=CategoryResponse)
def update_category_endpoint(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db)
    ):

    return update_category(db, category_id, category_data)