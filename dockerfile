# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
