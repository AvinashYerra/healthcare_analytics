import streamlit as st


def render_sidebar():

    st.sidebar.title("Healthcare Analytics")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Overview",
            "Patients",
            "Providers",
            "Organizations",
            "ETL Monitor",
        ],
    )

    return page