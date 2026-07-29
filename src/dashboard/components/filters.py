import streamlit as st

from analytics.analytics_service import AnalyticsService


def render_filters(service):

    genders = ["All"] + list(
        service.execute(
            "patients",
            "available_genders",
        )["GENDER"]
    )

    organizations = ["All"] + list(
        service.execute(
            "organizations",
            "available_organizations",
        )["NAME"]
    )

    gender = st.sidebar.selectbox(
        "Gender",
        genders,
    )

    organization = st.sidebar.selectbox(
        "Organization",
        organizations,
    )


    return {
        "gender": gender,
        "organization": organization,
    }