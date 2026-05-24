from app.database import Base

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import(
    Integer,
    String,
    DateTime,
)

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True)

    name: Mapped[str] = mapped_column(
        String(255), 
        nullable=False)
    
    phone: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        index=True,
        nullable=True
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