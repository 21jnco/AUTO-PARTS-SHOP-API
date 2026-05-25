from app.database import Base, engine

from app.models.category import Category
from app.models.product import Product
from app.models.customer import Customer
from app.models.order import Order
from app.models.order_item import OrderItem

def create_all_tables():
    Base.metadata.create_all(engine)
    print("Database created successfully")

if __name__ == "__main__":
    create_all_tables()