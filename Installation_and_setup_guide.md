# Installation and Setup Guide

Follow these steps to set up and run the Countries Information API project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Step 1: Install Required Packages

Install all the required packages using pip:

```bash
pip install django djangorestframework requests django-cors-headers django-filter
```

## Step 2: Apply Database Migrations

Create and apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 3: Create an Admin User

Create a superuser to access the admin interface and authenticated APIs:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

## Step 4: Fetch Country Data

Run the custom management command to fetch data from the REST Countries API:

```bash
python manage.py fetch_countries
```

This will:
- Connect to https://restcountries.com/v3.1/all
- Fetch data for all countries
- Parse and store the data in your database

## Step 5: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at:
- Web interface: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/

## Step 6: Access the Application

1. Open your web browser and go to http://127.0.0.1:8000/
2. You will be redirected to the login page
3. Enter the superuser credentials you created earlier
4. After logging in, you will see the Countries Information dashboard

## Troubleshooting

If you encounter any issues during installation or setup:

1. **Database Migration Errors**
   - Delete the db.sqlite3 file (if it exists)
   - Delete all files in the migrations folders except `__init__.py`
   - Run `python manage.py makemigrations myapp` followed by `python manage.py migrate`

2. **API Connection Issues**
   - Check your internet connection
   - Verify that https://restcountries.com is accessible from your network
   - Try running with `python manage.py fetch_countries --verbosity 2` for more detailed logs

3. **Missing static files**
   - Run `python manage.py collectstatic`
   - Ensure your STATIC_URL and STATICFILES_DIRS settings are correct

4. **Permission Denied Errors**
   - Make sure you are logged in with a valid user account
   - Check that the user has appropriate permissions
