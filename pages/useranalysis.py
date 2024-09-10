import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the page configuration
st.set_page_config(page_title="User Analysis Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

st.title("User Analysis Dashboard")

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)  # Adjust if you're using Excel or another format
    return data

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if upload_file is None:
        st.info("Please upload a file", icon="ℹ️")
        st.stop()

df = load_data(upload_file)

col1, col2, col3 = st.columns([1, 1, 1])

# User Overview Analysis
with col1.expander("User Overview"):
    st.dataframe(df)

    user_info = df.describe()
    st.write(user_info)

# User Engagement Analysis
engagement_data = df.groupby('Engagement_Score').size().reset_index(name='count')
with col2.expander("User Engagement Analysis"):
    st.write("Engagement Score Distribution")
    fig_engagement = px.histogram(engagement_data, x='Engagement_Score', y='count', title='Engagement Score Distribution')
    st.plotly_chart(fig_engagement, use_container_width=True)

# User Experience Analysis
experience_data = df.groupby('Experience_Score').size().reset_index(name='count')
with col3.expander("User Experience Analysis"):
    st.write("Experience Score Distribution")
    fig_experience = px.histogram(experience_data, x='Experience_Score', y='count', title='Experience Score Distribution')
    st.plotly_chart(fig_experience, use_container_width=True)

# Satisfaction Analysis
satisfaction_data = df.groupby('Satisfaction_Score').size().reset_index(name='count')
with col1.expander("User Satisfaction Analysis"):
    st.write("Satisfaction Score Distribution")
    fig_satisfaction = px.histogram(satisfaction_data, x='Satisfaction_Score', y='count', title='Satisfaction Score Distribution')
    st.plotly_chart(fig_satisfaction, use_container_width=True)

# Additional Metrics
col3.metric(label="Total Users", value=len(df))