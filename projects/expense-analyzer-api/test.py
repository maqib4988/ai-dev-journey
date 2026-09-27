from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

app = FastAPI()


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    return {"filename": file.filename, "rows": len(df), "columns": list(df.columns)}


@app.post("/analyze-expenses")
async def analyze_expenses(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    required_columns = {"date", "category", "amount"}
    if not required_columns.issubset(df.columns):
        return {"error": f"CSV must contain columns: {required_columns}"}

    total_spent = float(df["amount"].sum())
    avg_expense = float(df["amount"].mean())
    highest_expense = float(df["amount"].max())

    spend_by_category = df.groupby("category")["amount"].sum().to_dict()
    spend_by_category = {k: float(v) for k, v in spend_by_category.items()}

    top_category = max(spend_by_category, key=spend_by_category.get)
    count_by_category = df.groupby("category").size().to_dict()

    return {
        "total_transactions": len(df),
        "total_spent": round(total_spent, 2),
        "average_expense": round(avg_expense, 2),
        "highest_expense": round(highest_expense, 2),
        "spend_by_category": spend_by_category,
        "top_spending_category": top_category,
        "transactions_per_category": count_by_category,
    }
