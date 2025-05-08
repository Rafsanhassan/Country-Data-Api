# Country Data Explorer

A Django-based web application for exploring and viewing country information. This project features a RESTful API and a web interface with authentication to display detailed information about countries around the world.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Development Phases](#development-phases)

## Features

- Display comprehensive information about countries including:
  - Name, country code, capital
  - Population, timezone, region
  - Flag, languages spoken
- Search functionality to find countries by name
- Detailed view showing regional countries and languages
- RESTful API for programmatic access to country data
- Authentication system to restrict access to authorized users
- Responsive design using Bootstrap

## Project Structure

```
assignment/
  ├── assignment/         # Project settings directory
  │   ├── __init__.py
  │   ├── settings.py     # Project settings
  │   ├── urls.py         # Main URL configuration
  │   ├── wsgi.py
  │   └── asgi.py
  ├── myapp/              # Main application directory
  │   ├── __init__.py
  │   ├── admin.py        # Admin configuration
  │   ├── apps.py
  │   ├── models.py       # Country data model
  │   ├── serializers.py  # API serializers
  │   ├── urls.py         # App URL configuration
  │   ├── views.py        # Views and API viewsets
  │   ├── management/     # Custom management commands
  │   │   ├── __init__.py
  │   │   └── commands/
  │   │       ├── __init__.py
  │   │       ├── import_countries.py     # Command to import country data
  │   │       └── create_test_user.py     # Command to create test users
  │   ├── static/
  │   │   └── myapp/
  │   │       └── images/
  │   │           └── placeholder-flag.svg   # Placeholder flag image
  │   └── templates/     # HTML templates
  │       ├── myapp/
  │       │   └── index.html              # Main country list template
  │       └── registration/
  │           ├── login.html              # Login page template
  │           └── logged_out.html         # Logout confirmation template
  ├── manage.py          # Django management script
  └── requirements.txt   # Project dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd assignment
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a test user:
   ```bash
   python manage.py create_test_user
   ```
   This creates a user with username `admin` and password `password123`

7. Import country data:
   ```bash
   python manage.py import_countries
   ```

## Usage

### Running the Server

Start the development server:
```bash
python manage.py runserver
```

Access the application at http://localhost:8000/

### Accessing the Application

1. Navigate to http://localhost:8000/
2. You'll be redirected to the login page
3. Log in with:
   - Username: `admin`
   - Password: `password123`
4. After logging in, you'll see the list of countries
5. Use the search box to find countries by name
6. Click the "Details" button to view more information about a specific country

### Admin Interface

Access the Django admin interface at http://localhost:8000/admin/ to manage users and country data.

## API Endpoints

All API endpoints require authentication.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/countries/` | GET | List all countries |
| `/api/countries/?search=term` | GET | Search countries by name |
| `/api/countries/{cca2}/` | GET | Get details for a specific country |
| `/api/countries/{cca2}/regional_countries/` | GET | Get countries in the same region |
| `/api/countries/{cca2}/languages/` | GET | Get languages spoken in the country |

### API Usage Examples

Using cURL with authentication:
```bash
curl -u admin:password123 http://localhost:8000/api/countries/
```

## Authentication

The application uses Django's built-in authentication system:

- All views and API endpoints are restricted to authenticated users
- Session-based authentication for web interface
- Basic authentication for API access
- Custom styled login/logout pages

### Creating Additional Users

Create a superuser account:
```bash
python manage.py createsuperuser
```

Then access the admin interface at http://localhost:8000/admin/ to manage users.

## Development Phases

This project was developed in four main phases:

### Phase 1: Data Model

- Designed and implemented the Country model
- Created management command to import country data from the REST Countries API
- Implemented data validation and basic error handling

### Phase 2: REST API

- Implemented RESTful API with Django REST Framework
- Created serializers for country data
- Added search functionality
- Implemented filtering and detailed endpoints for country information

### Phase 3: Web Interface

- Designed and implemented a responsive web interface using Bootstrap
- Created templates for displaying country information
- Implemented search functionality in the UI
- Added detailed view with regional countries and languages

### Phase 4: Authentication and Security

- Implemented authentication using Django's built-in User model
- Restricted API access to authenticated users
- Created login/logout pages
- Added security features like CSRF protection and secure password validation

## License

[Include your license information here]

## Contributors

[Include contributor information here]
