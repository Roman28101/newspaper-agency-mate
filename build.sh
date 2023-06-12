#!/usr/bin/env bash
# exit on error
# Start of the build process
echo "Starting the build process..."

# Run some commands
echo "Running command 1..."
set -o errexit

echo "Running command 2..."
pip install -r requirements.txt

echo "Running command 3..."
python manage.py collectstatic --no-input

echo "Running command 4..."
python manage.py migrate

# Display a success message
echo "Build process completed successfully!"





