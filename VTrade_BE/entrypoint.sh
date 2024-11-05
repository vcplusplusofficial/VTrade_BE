#!/bin/sh

echo "Waiting for the database to be ready..."

# Loop until the database becomes accessible
while ! nc -z db 5432; do
  echo "Database is not ready. Retrying in 2 seconds..."
  sleep 2
done

# Read the database password from the secret file
DB_PASSWORD=$(cat /run/secrets/db_password)

echo "Running migrations..."
export DB_PASSWORD

# Apply Django migrations
python manage.py migrate

echo "Starting Django server..."
exec "$@"
