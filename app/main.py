from fastapi import FastAPI

from app.routers.category_router import router as category_router
from app.routers.customer_router import router as customer_router
from app.routers.product_router import router as product_router
from app.routers.order_router import router as order_router

app = FastAPI(
    title="Auto Parts Shop API",
    version="1.0.0"
)

app.include_router(category_router)
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)
