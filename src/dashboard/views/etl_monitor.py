import streamlit as st
import plotly.express as px
from analytics.metrics_reader import MetricsReader


st.title("ETL Monitor")

def show_etl_monitor(filters=None):



    reader = MetricsReader()
    df = reader.load()

    if df.empty:
        st.warning("No pipeline metrics found.")
        return

    total = len(df)
    success = (df["status"] == "SUCCESS").sum()
    failed = total - success
    runtime = round(df["execution_time"].sum(), 2)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Pipelines", total)
    c2.metric("Successful", success)
    c3.metric("Failed", failed)
    c4.metric("Runtime (sec)", runtime)

    st.subheader("Pipeline Status")

    df = df[
        [
            "dataset",
            "layer",
            "status",
            "input_records",
            "output_records",
            "execution_time",
            "timestamp",
        ]
    ]
    df = df.rename(
    columns={
        "dataset": "Pipeline",
        "layer": "Layer",
        "status": "Status",
        "input_records": "Input",
        "output_records": "Output",
        "execution_time": "Time (sec)",
        "timestamp": "Last Run",
    }
)
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )


    fig = px.bar(
    df,
    x="Pipeline",
    y="Time (sec)",
    title="Pipeline Execution Time",
)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    record_df = df[
    ["Pipeline", "Input", "Output"]
]

    fig = px.bar(
        record_df,
        x="Pipeline",
        y=["Input", "Output"],
        barmode="group",
        title="Input vs Output Records",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )