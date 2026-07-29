import streamlit as st

from analytics.analytics_service import AnalyticsService
from dashboard.components.charts import bar_chart



def show_organizations(filters):

    st.title("Organizations")

    service = AnalyticsService()

    organizations = service.execute(
        "organizations",
        "top_organizations",
    )

    chart = bar_chart(
        organizations,
        "NAME",
        "total_encounters",
        "Top Organizations",
        horizontal=True,
    )

    st.plotly_chart(
        chart,
        use_container_width=True,
    )
