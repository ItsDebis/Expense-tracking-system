import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"


def add_update_tab():
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key=f"expense_form_{selected_date}"):
        col1, col2, col3 = st.columns(3)
        col1.text("Amount")
        col2.text("Category")
        col3.text("Notes")

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)

            with col1:
                amount_input = st.number_input(
                    "Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"amount_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

            with col2:
                category_input = st.selectbox(
                    "Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                notes_input = st.text_input(
                    "Notes",
                    value=notes,
                    key=f"notes_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit = st.form_submit_button("Submit")

        if submit:
            filtered_expenses = [
                e for e in expenses if e["amount"] > 0
            ]

            response = requests.post(
                f"{API_URL}/expenses/{selected_date}",
                json=filtered_expenses
            )

            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")
