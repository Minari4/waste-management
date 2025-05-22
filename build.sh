#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r smart-waste-management/requirements.txt

# Create necessary directories
mkdir -p smart-waste-management/staticfiles
mkdir -p smart-waste-management/media

# Add project directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)/smart-waste-management

# Collect static files
cd smart-waste-management
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate 