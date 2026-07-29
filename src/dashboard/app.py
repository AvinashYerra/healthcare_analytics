import streamlit as st

from dashboard.utils.sidebar import render_sidebar

from dashboard.views.overview import show_overview
from dashboard.views.patients import show_patients
from dashboard.views.providers import show_providers
from dashboard.views.organizations import show_organizations
from dashboard.views.etl_monitor import show_etl_monitor
from dashboard.components.filters import render_filters
from analytics.analytics_service import AnalyticsService

st.set_page_config(
    page_title="Healthcare Analytics",
    page_icon="🏥",
    layout="wide",
)

service = AnalyticsService()

page = render_sidebar()
# filters = render_filters(service)
filters = None

if page == "Overview":
    show_overview(filters, service)

elif page == "Patients":
    show_patients(filters)

elif page == "Providers":
    show_providers(filters)

elif page == "Organizations":
    show_organizations(filters)

elif page == "ETL Monitor":
    show_etl_monitor(filters)