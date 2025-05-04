
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e9f256f (Update README.md)
# Countries Information API

This Django application fetches and displays data about countries from the REST Countries API. It provides both a web interface and RESTful API endpoints for accessing country information.

## Features

- Fetches data from [REST Countries API](https://restcountries.com/v3.1/all)
- Stores country data in a Django model
- Provides RESTful API endpoints for accessing the data
- Secured web interface with authentication
- Search and filter functionality
- Responsive design

## Setup Instructions

### 1. Install Required Packages

```bash
pip install django djangorestframework requests django-cors-headers django-filter
```

### 2. Configure the Application

The project is already set up with the necessary configurations in `settings.py`.

### 3. Apply Migrations

Create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

Create an admin user to access the secured features:

```bash
python manage.py createsuperuser
```

### 5. Fetch Country Data

Run the management command to fetch country data from the REST Countries API:

```bash
python manage.py fetch_countries
```

### 6. Run Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Project Structure

- `models.py`: Defines the `Country` model with all relevant fields
- `views.py`: Contains web views and API endpoints
- `urls.py`: Defines URL routing
- `serializers.py`: Provides JSON serialization for the API
- `admin.py`: Registers models with the Django admin interface
- `management/commands/fetch_countries.py`: Management command to fetch data

## API Endpoints

All API endpoints require authentication.

- `GET /api/countries/`: List all countries (paginated)
- `GET /api/countries/<id>/`: Get details for a specific country by ID
- `GET /api/country/<code>/`: Get details for a country by code (CCA2 or CCA3)
- `GET /api/regions/`: Get list of unique regions
- `GET /api/search/?q=<term>`: Search countries by name

## Authentication

The API and the web interface are secured using Django's authentication system. You can:

1. Login at the `/login/` endpoint
2. Use Django REST Framework's session authentication
3. Use Basic Authentication for API requests

## Testing

Run tests with:

```bash
python manage.py test
```
<<<<<<< HEAD
=======
>>>>>>> commit123
=======
>>>>>>> e9f256f (Update README.md)
