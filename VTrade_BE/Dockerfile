# Pull base image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies required by Django and PostgreSQL
RUN apt-get update && apt-get install -y \
    netcat libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code

# Copy requirements file and install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Ensure the entrypoint.sh script is executable
RUN chmod +x /code/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
