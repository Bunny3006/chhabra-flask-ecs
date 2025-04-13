# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install flask

# Run the application
CMD ["python", "app.py"]

