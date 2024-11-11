#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Wait until PostgreSQL is ready
echo "Waiting for PostgreSQL to start..."
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  echo "PostgreSQL not yet available, retrying in 0.5 seconds..."
  sleep 0.5
done
echo "PostgreSQL started."

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files (optional, uncomment if needed)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Execute the command passed to the container (in this case, Django's runserver command from docker-compose.yml)
exec "$@"
