from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    return db_helper.fetch_expenses_for_date(expense_date)


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)

    for expense in expenses:
        db_helper.insert_expense(
            expense_date,
            expense.amount,
            expense.category,
            expense.notes
        )

    return {"message": "Expenses updated successfully"}


@app.post("/analytics/")
def category_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(
        date_range.start_date,
        date_range.end_date
    )

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    total_sum = sum(row["total"] for row in data)

    return {
        row["category"]: {
            "total": row["total"],
            "percentage": (row["total"] / total_sum) * 100
        }
        for row in data
    }


@app.get("/analytics/monthly-summary/{year}")
def monthly_summary(year: int):
    data = db_helper.fetch_monthly_summary_by_year(year)

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    return data

