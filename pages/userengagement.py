
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="User Engagement Analysis",
                   page_icon=":bar_chart:",
                   layout="wide")

# Set page title
st.title("User Engagement Analysis")

# Load sample data (replace with your actual data loading method)
data = {
    'User': ['User A', 'User B', 'User C', 'User D'],
    'Engagement_Score': [70, 85, 90, 75],
}
df = pd.DataFrame(data)

# Display the data
st.subheader("User Engagement Data")
st.dataframe(df)

# Create a slider for filtering engagement scores
min_score, max_score = st.slider("Select Engagement Score Range", 0, 100, (50, 100))

# Filter the DataFrame based on the score range
filtered_df = df[(df['Engagement_Score'] >= min_score) & (df['Engagement_Score'] <= max_score)]

# Display filtered data
st.write("Filtered Data:")
st.dataframe(filtered_df)

# Plotting the engagement scores
fig = px.bar(filtered_df, x='User', y='Engagement_Score', 
              title='User Engagement Scores', 
              labels={'Engagement_Score': 'Engagement Score', 'User': 'User'})
st.plotly_chart(fig)

# Additional metrics
st.subheader("Engagement Score Statistics")
st.write(f"Average Engagement Score: {filtered_df['Engagement_Score'].mean():.2f}")
st.write(f"Minimum Engagement Score: {filtered_df['Engagement_Score'].min()}")
st.write(f"Maximum Engagement Score: {filtered_df['Engagement_Score'].max()}")