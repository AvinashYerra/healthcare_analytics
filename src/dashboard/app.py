import streamlit as st

from dashboard.utils.sidebar import render_sidebar

from dashboard.pages.overview import show_overview
from dashboard.pages.patients import show_patients
from dashboard.pages.providers import show_providers
from dashboard.pages.organizations import show_organizations
from dashboard.pages.etl_monitor import show_etl_monitor


st.set_page_config(
    page_title="Healthcare Analytics",
    page_icon="🏥",
    layout="wide",
)

page = render_sidebar()

if page == "Overview":
    show_overview()

elif page == "Patients":
    show_patients()

elif page == "Providers":
    show_providers()

elif page == "Organizations":
    show_organizations()

else:
    show_etl_monitor()