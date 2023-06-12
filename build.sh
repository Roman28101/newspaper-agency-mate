#!/usr/bin/env bash
# exit on error
# Start of the build process
echo "Starting the build process..."

# Run some commands
echo "Running command 1..."
command1

echo "Running command 2..."
command2

# Display a success message
echo "Build process completed successfully!"
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate