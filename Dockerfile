# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
