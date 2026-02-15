import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def monthly_analytics_tab():
    st.subheader("Expense Breakdown By Months")

    year = st.selectbox("Select Year", [2023, 2024, 2025], index=1)

    if st.button("Get Monthly Analytics"):
        response = requests.get(
            f"{API_URL}/analytics/monthly-summary/{year}"
        )

        if response.status_code != 200:
            st.error("No data found")
            return

        df = pd.DataFrame(response.json())
        df = df.sort_values("month")

        st.bar_chart(df.set_index("month_name")["total"], use_container_width=True)

        df["total"] = df["total"].map("{:.2f}".format)
        st.table(df[["month_name", "total"]])
