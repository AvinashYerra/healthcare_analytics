import streamlit as st

from analytics.analytics_service import AnalyticsService
from dashboard.components.charts import bar_chart


def show_providers(filters):

    st.title("Providers")
    service = AnalyticsService()


    providers = service.execute(
        "providers",
        "top_providers",
    )

    chart = bar_chart(
        providers,
        "NAME",
        "total_encounters",
        "Top Providers",
        horizontal=True,
    )

    st.plotly_chart(
        chart,
        use_container_width=True,
    )