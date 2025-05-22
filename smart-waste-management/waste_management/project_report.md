# Smart Waste Management Project Report

## Project Overview
This project is a Django-based web application for managing waste bins, collection routes, and illegal dumping reports. It includes user authentication, a dashboard, and various administrative features.

## Project Structure
- **Root Directory**: smart-waste-management
  - **waste_management**: Main project directory
    - **manage.py**: Django's command-line utility for administrative tasks.
    - **waste_management/**: Core project settings directory
      - **settings.py**: Project settings including installed apps, middleware, and database configuration.
      - **urls.py**: Main URL routing configuration.
      - **wsgi.py**: WSGI application entry point.
      - **asgi.py**: ASGI application entry point.
      - **__init__.py**: Empty file, no project-level code.
    - **accounts/**: User authentication and profile management
      - **models.py**: No custom models defined.
      - **views.py**: Contains views for login, logout, signup, and profile management.
      - **urls.py**: URL routing for accounts app.
      - **admin.py**: Admin configuration for accounts app.
      - **apps.py**: App configuration for accounts app.
      - **tests.py**: Test cases for accounts app.
    - **dashboard/**: Dashboard functionality
      - **models.py**: Defines a DashboardWidget model.
      - **views.py**: Contains views for displaying the dashboard, including bin data and environmental reminders.
      - **urls.py**: URL routing for dashboard app.
      - **admin.py**: Admin configuration for dashboard app.
      - **apps.py**: App configuration for dashboard app.
      - **tests.py**: Test cases for dashboard app.
    - **bins/**: Waste bin management
      - **models.py**: Defines a WasteBin model with fields for identifier, bin type, location, latitude, longitude, current status, and last collected timestamp.
      - **views.py**: Contains views for listing, creating, editing, and deleting waste bins.
      - **urls.py**: URL routing for bins app.
      - **admin.py**: Admin configuration for bins app.
      - **apps.py**: App configuration for bins app.
      - **tests.py**: Test cases for bins app.
    - **routes/**: Collection route management
      - **models.py**: Defines models for Bin, CollectionRoute, and RouteBin.
      - **views.py**: Contains views for listing, creating, editing, and deleting collection routes.
      - **urls.py**: URL routing for routes app.
      - **admin.py**: Admin configuration for routes app.
      - **apps.py**: App configuration for routes app.
      - **tests.py**: Test cases for routes app.
    - **reports/**: Illegal dumping report management
      - **models.py**: Defines an IllegalDumpingReport model with fields for reporter, location, latitude, longitude, description, photo, status, reported_at, updated_at, and notes.
      - **views.py**: Contains views for listing, creating, editing, and deleting illegal dumping reports.
      - **urls.py**: URL routing for reports app.
      - **admin.py**: Admin configuration for reports app.
      - **apps.py**: App configuration for reports app.
      - **tests.py**: Test cases for reports app.
    - **templates/**: Directory for HTML templates.
    - **staticfiles/**: Directory for collected static files.
    - **static/**: Directory for static files (CSS, JavaScript, images).
    - **media/**: Directory for user-uploaded media files.
    - **.pytest_cache/**: Directory for pytest cache files.
    - **db.sqlite3**: SQLite database file.

## Key Features
- User authentication and profile management.
- Dashboard displaying waste bin data and environmental reminders.
- Waste bin management (create, edit, delete, list).
- Collection route management (create, edit, delete, list).
- Illegal dumping report management (create, edit, delete, list).

## Technologies Used
- Django: Web framework.
- SQLite: Database.
- HTML/CSS/JavaScript: Frontend.
- pytest: Testing framework.

## Conclusion
This project provides a comprehensive solution for managing waste bins, collection routes, and illegal dumping reports. It is built using Django and includes various features for user authentication, dashboard functionality, and administrative tasks. 