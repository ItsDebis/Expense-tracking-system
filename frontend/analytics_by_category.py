import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)

        if response.status_code != 200:
            st.error("No data found")
            return

        data = response.json()

        df = pd.DataFrame({
            "Category": data.keys(),
            "Total": [v["total"] for v in data.values()],
            "Percentage": [v["percentage"] for v in data.values()]
        })

        df = df.sort_values("Percentage", ascending=False)

        st.bar_chart(df.set_index("Category")["Percentage"], use_container_width=True)

        df["Total"] = df["Total"].map("{:.2f}".format)
        df["Percentage"] = df["Percentage"].map("{:.2f}".format)

        st.table(df)
