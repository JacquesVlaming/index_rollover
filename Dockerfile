# Use an official Python base image
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

# Copy your script into the container
COPY rollover_streams_v0.1.py .

# Command to run the script
CMD ["python", "rollover_streams_v0.1.py"]
