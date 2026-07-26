import plotly.express as px


def bar_chart(
    dataframe,
    x,
    y,
    title,
    horizontal=False,
):

    if horizontal:
        return px.bar(
            dataframe,
            x=y,
            y=x,
            orientation="h",
            title=title,
        )

    return px.bar(
        dataframe,
        x=x,
        y=y,
        title=title,
    )