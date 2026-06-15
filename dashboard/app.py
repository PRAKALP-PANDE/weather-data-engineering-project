import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Weather Analytics Dashboard",
    layout="wide"
)

st.title("🌤 Weather Analytics Dashboard")

avg_temp = pd.read_csv(
    "dashboard/data/avg_temperature.csv"
)

avg_humidity = pd.read_csv(
    "dashboard/data/avg_humidity.csv"
)

max_temp = pd.read_csv(
    "dashboard/data/max_temperature.csv"
)
# KPI Section

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Temperature",
        round(avg_temp["avg_temperature"].mean(), 2)
    )

with col2:
    st.metric(
        "Maximum Temperature",
        round(max_temp["max_temperature"].max(), 2)
    )

with col3:
    st.metric(
        "Average Humidity",
        round(avg_humidity["avg_humidity"].mean(), 2)
    )

with col4:
    st.metric(
        "Cities Tracked",
        len(avg_temp)
    )

# Temperature Chart

st.subheader(
    "Average Temperature by City (°C)"
)

st.bar_chart(
    avg_temp.set_index("city")
)

# Humidity Chart

st.subheader(
    "Average Humidity by City (%)"
)

st.bar_chart(
    avg_humidity.set_index("city")
)

# Maximum Temperature Chart

st.subheader(
    "Maximum Temperature by City"
)

st.bar_chart(
    max_temp.set_index("city")
)


# Add Project Description
st.markdown(
    """
    End-to-end Weather Data Engineering Pipeline
    built using Python, Docker, Databricks,
    PySpark, Delta Lake, and Streamlit.
    """
)

# Add Last Refresh Timestamp
from datetime import datetime

st.caption(
    f"Last Updated: {datetime.now()}"
)


# Weather Summary Table
summary_df = avg_temp.merge(
    avg_humidity,
    on="city"
).merge(
    max_temp,
    on="city"
)

st.subheader("City Weather Summary")
st.dataframe(summary_df)