import streamlit as st

from analytics.analytics_service import AnalyticsService
from dashboard.components.charts import bar_chart


def show_overview(filters, service):

    patients = service.execute(
        "overview",
        "total_patients",
        filters,
    ).iloc[0, 0]

    providers = service.execute(
        "overview",
        "total_providers",
        filters,
    ).iloc[0, 0]

    organizations = service.execute(
        "overview",
        "total_organizations",
        filters,
    ).iloc[0, 0]

    st.title("Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Patients",
        patients,
    )

    c2.metric(
        "Providers",
        providers,
    )

    c3.metric(
        "Organizations",
        organizations,
    )

    gender = service.execute(
        "patients",
        "gender_distribution",
        filters,
    )


    provider_df = service.execute(
        "providers",
        "top_providers",
        filters,
    )

    organization_df = service.execute(
        "organizations",
        "top_organizations",
        filters,
    )


    gender_chart = bar_chart(
        gender,
        "GENDER",
        "patients",
        "Gender Distribution",
    )

    provider_chart = bar_chart(
        provider_df,
        "NAME",
        "total_encounters",
        "Top Providers",
        horizontal=True,
    )


    organization_chart = bar_chart(
        organization_df,
        "NAME",
        "total_encounters",
        "Top Organizations",
        horizontal=True,
    )


    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            gender_chart,
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            provider_chart,
            use_container_width=True,
        )

    st.plotly_chart(
        organization_chart,
        use_container_width=True,
    )
