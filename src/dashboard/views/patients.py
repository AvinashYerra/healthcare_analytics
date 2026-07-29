import streamlit as st

from analytics.analytics_service import AnalyticsService
from dashboard.components.charts import bar_chart


def show_patients(filters):

    st.title("Patients")

    service = AnalyticsService()

    gender = service.execute(
        "patients",
        "gender_distribution",
    )

    chart = bar_chart(
        gender,
        "GENDER",
        "patients",
        "Gender Distribution",
    )

    st.plotly_chart(
        chart,
        use_container_width=True,
    )
