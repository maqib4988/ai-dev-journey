from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    category: str
    amount: float
    note: str = ""


@app.get("/")
def read_root():
    return {"message": "Hello from your first API"}


@app.post("/expense")
def create_expense(expense: Expense):
    return {
        "received": expense.model_dump(),
        "message": f"Logged {expense.amount} under {expense.category}",
    }
