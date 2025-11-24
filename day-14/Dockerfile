# Start from the base Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install dependencies, ensuring no cache and upgrading packages
# (The speaker mentions using --no-cache-dir and --upgrade for demonstration)
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the local 'app' directory contents (including main.py) into the container's working directory
COPY app/ .

# Command to run the uvicorn server, binding to all interfaces on port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]