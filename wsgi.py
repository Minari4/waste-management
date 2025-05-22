import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'smart-waste-management'))

from waste_management.wsgi import application 