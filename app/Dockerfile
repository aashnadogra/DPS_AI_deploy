# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and dataset into the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 8080

# Command to run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
