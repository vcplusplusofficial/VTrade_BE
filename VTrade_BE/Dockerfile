# Pull base image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat && apt-get clean

# Set work directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

EXPOSE 8000

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Command to run your application
#letting docker comopse handle this
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
