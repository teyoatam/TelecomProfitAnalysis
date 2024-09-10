import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="User Satisfaction Analysis",
                   page_icon=":bar_chart:",
                   layout="wide")

# Set page title
st.title("User Satisfaction Analysis")

# Load sample data (replace with your actual data loading method)
data = {
    'User': ['User A', 'User B', 'User C', 'User D'],
    'Satisfaction_Score': [90, 85, 80, 88],
}
df = pd.DataFrame(data)

# Display the data
st.subheader("User Satisfaction Data")
st.dataframe(df)

# Create a slider for filtering satisfaction scores
min_score, max_score = st.slider("Select Satisfaction Score Range", 0, 100, (70, 100))

# Filter the DataFrame based on the score range
filtered_df = df[(df['Satisfaction_Score'] >= min_score) & (df['Satisfaction_Score'] <= max_score)]

# Display filtered data
st.write("Filtered Data:")
st.dataframe(filtered_df)

# Plotting the satisfaction scores
fig = px.pie(filtered_df, names='User', values='Satisfaction_Score', 
              title='User Satisfaction Distribution', 
              labels={'Satisfaction_Score': 'Satisfaction Score'})
st.plotly_chart(fig)

# Additional metrics
st.subheader("Satisfaction Score Statistics")
st.write(f"Average Satisfaction Score: {filtered_df['Satisfaction_Score'].mean():.2f}")
st.write(f"Minimum Satisfaction Score: {filtered_df['Satisfaction_Score'].min()}")
st.write(f"Maximum Satisfaction Score: {filtered_df['Satisfaction_Score'].max()}")