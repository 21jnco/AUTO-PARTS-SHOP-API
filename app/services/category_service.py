from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


def create_category(db: Session, category_data: CategoryCreate):
    query = select(Category).where(Category.name == category_data.name)
    result = db.execute(query)

    category_exists = result.scalar_one_or_none()

    if category_exists is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category with this name already exists."
        )
    
    category = Category(
        name=category_data.name,
        description=category_data.description
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def update_category(db: Session, category_id: int, category_data: CategoryUpdate):
    query = select(Category).where(Category.id == category_id)
    result = db.execute(query)

    category = result.scalar_one_or_none()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )
    
    if category_data.name is not None:
        category.name = category_data.name

    if category_data.description is not None:
        category.description = category_data.description

    db.commit()
    db.refresh(category)

    return category


def get_all_categories(db: Session):
    query = select(Category)
    result = db.execute(query)

    return result.scalars().all()


def get_category_by_id(db: Session, category_id: int):
    query = select(Category).where(Category.id == category_id)
    result = db.execute(query)

    category = result.scalar_one_or_none()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found."
        )
    
    return category