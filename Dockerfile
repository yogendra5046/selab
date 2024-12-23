# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
