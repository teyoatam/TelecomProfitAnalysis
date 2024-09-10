FROM python:3.9-slim

# Set working directory
WORKDIR /tests

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .

# Expose the port for MLflow
EXPOSE 5000

# Command to run MLflow
CMD ["mlflow", "ui", "--host", "0.0.0.0"]