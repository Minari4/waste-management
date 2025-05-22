#!/bin/bash

# Exit on error
set -e

# Update system packages
echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

# Install required system packages
echo "Installing system dependencies..."
sudo apt-get install -y python3-pip python3-dev nginx postgresql postgresql-contrib

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create systemd service file
echo "Creating systemd service..."
sudo tee /etc/systemd/system/smart_waste_management.service << EOF
[Unit]
Description=Smart Waste Management Gunicorn Service
After=network.target

[Service]
User=$USER
Group=www-data
WorkingDirectory=$(pwd)
Environment="PATH=$(pwd)/venv/bin"
ExecStart=$(pwd)/venv/bin/gunicorn --config gunicorn_config.py waste_management.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

# Configure Nginx
echo "Configuring Nginx..."
sudo tee /etc/nginx/sites-available/smart_waste_management << EOF
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root $(pwd);
    }

    location /media/ {
        root $(pwd);
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/smart_waste_management.sock;
    }
}
EOF

# Enable the site
sudo ln -s /etc/nginx/sites-available/smart_waste_management /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

# Start and enable the service
echo "Starting the application..."
sudo systemctl start smart_waste_management
sudo systemctl enable smart_waste_management

echo "Deployment completed successfully!" 