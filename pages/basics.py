
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="User Analysis Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

# Set page title
st.title("User Analysis Dashboard")

# ### Text Input

# Create a text input field for user name
user_name = st.text_input("Enter your name", placeholder="Your Name")

# Display the input text
st.write("Hello, " + user_name + "!")

# ### Slider for Engagement Score

# Create a slider for engagement score
engagement_score = st.slider("Select your Engagement Score", 0, 100, 50, step=1)

# Display the selected engagement score
st.write("Your Engagement Score:", engagement_score)

# ### Button to Submit Feedback

# Create a button for feedback submission
submit_feedback = st.button("Submit Feedback")

# Handle button click
if submit_feedback:
    st.success("Thank you for your feedback!")

# ### Radio Buttons for Experience Rating

# Create radio buttons for experience rating
experience_rating = st.radio("Rate your experience", ["Very Poor", "Poor", "Average", "Good", "Excellent"])

# Display the selected rating
st.write("Your Experience Rating:", experience_rating)

# ### Checkboxes for Features Used

# Create checkboxes for features used
features_used = st.multiselect("Select features you used", ["Feature A", "Feature B", "Feature C", "Feature D"])

# Display the selected features
st.write("Features Used:", features_used)

# ### Date Input for Feedback Date

# Create a date input for feedback date
feedback_date = st.date_input("Select feedback date")

# Display the selected date
st.write("Feedback Date:", feedback_date)

# ### Upload Feedback File

# Create a file uploader for uploading feedback files
uploaded_file = st.file_uploader("Upload feedback file (optional)", type=["csv", "xlsx"])

# Process and display the uploaded file
if uploaded_file is not None:
    # Read the file into a DataFrame
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("Uploaded Feedback Data:")
    st.dataframe(df)

# ### Summary Section

st.header("Summary of Your Analysis")
st.write("Name:", user_name)
st.write("Engagement Score:", engagement_score)
st.write("Experience Rating:", experience_rating)
st.write("Features Used:", features_used)
st.write("Feedback Date:", feedback_date)