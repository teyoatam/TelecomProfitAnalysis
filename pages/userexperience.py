import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="User Experience Analysis",
                   page_icon=":bar_chart:",
                   layout="wide")

# Set page title
st.title("User Experience Analysis")

# Load sample data (replace with your actual data loading method)
data = {
    'User': ['User A', 'User B', 'User C', 'User D'],
    'Experience_Score': [80, 75, 95, 70],
}
df = pd.DataFrame(data)

# Display the data
st.subheader("User Experience Data")
st.dataframe(df)

# Create a slider for filtering experience scores
min_score, max_score = st.slider("Select Experience Score Range", 0, 100, (60, 100))

# Filter the DataFrame based on the score range
filtered_df = df[(df['Experience_Score'] >= min_score) & (df['Experience_Score'] <= max_score)]

# Display filtered data
st.write("Filtered Data:")
st.dataframe(filtered_df)

# Plotting the experience scores
fig = px.box(filtered_df, y='Experience_Score', 
              title='User Experience Scores', 
              labels={'Experience_Score': 'Experience Score'})
st.plotly_chart(fig)

# Additional metrics
st.subheader("Experience Score Statistics")
st.write(f"Average Experience Score: {filtered_df['Experience_Score'].mean():.2f}")
st.write(f"Minimum Experience Score: {filtered_df['Experience_Score'].min()}")
st.write(f"Maximum Experience Score: {filtered_df['Experience_Score'].max()}")