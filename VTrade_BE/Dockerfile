# Use the base image
FROM python:3.11.5-slim-bullseye

# Install system dependencies needed for cryptography, psycopg2, etc.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libssl-dev \
    libffi-dev \
    netcat && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port and set entrypoint
EXPOSE 8000
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
