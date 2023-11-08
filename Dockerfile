# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirement.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy all files from the current directory into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]