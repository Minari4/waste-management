#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r smart-waste-management/requirements.txt

# Collect static files
cd smart-waste-management
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate 