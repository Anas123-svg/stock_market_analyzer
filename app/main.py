from fastapi import FastAPI
from app.api import stock_routes

app = FastAPI(title="Stock Market Analysis")

app.include_router(stock_routes.router, prefix="/api/v1/stocks", tags=["Stocks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Market Analysis API!"}
