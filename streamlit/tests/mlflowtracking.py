import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load your dataset
data = pd.read_csv('user_scores_with_clusters.csv')

# Define features and target
X = data[['Engagement_Score', 'Experience_Score']]
y = data['Satisfaction_Score']

# Start tracking
mlflow.start_run()

# Log parameters
mlflow.log_param("model_type", "Linear Regression")
mlflow.log_param("data_source", "user_scores_with_clusters.csv")

# Train the model
model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Make predictions and log metrics
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mlflow.log_metric("mse", mse)

# Log the model
mlflow.sklearn.log_model(model, "linear_regression_model")

# End the run
mlflow.end_run()