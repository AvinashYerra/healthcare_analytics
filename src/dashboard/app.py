import streamlit as st

st.set_page_config(
    page_title="Healthcare Analytics",
    page_icon="🏥",
    layout="wide",
)

st.title("🏥 Healthcare Analytics Platform")

st.markdown(
    """
    End-to-End Healthcare Analytics built using

    - PySpark
    - DuckDB
    - Azure Data Lake
    - Airflow
    - Streamlit
    """
)

st.success("Select a page from the sidebar.")