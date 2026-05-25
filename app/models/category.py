from app.database import Base

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    Integer, 
    Boolean, 
    String,
    Text,
    DateTime
    )

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True)

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True)

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
        )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    products = relationship(
        "Product",
        back_populates="category"
    )
    