import streamlit as st


def show_etl_monitor():

    st.title("ETL Monitor")

    st.success("Bronze → Silver completed")

    st.success("Silver → Gold completed")

    st.success("Azure Upload completed")