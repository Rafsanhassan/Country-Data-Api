# Phase 4: Authentication and Security Implementation Guide

This guide will walk you through implementing authentication and security features for the Country Data Explorer project.

## Step 1: Set up Project Structure

First, make sure you have the necessary directory structure:

```bash
# Create the template directories
mkdir -p myapp/templates/registration
mkdir -p myapp/static/myapp/images
mkdir -p myapp/management/commands
```

## Step 2: Update Project Settings

Update your `settings.py` file with the authentication configuration:

1. Make sure `django.contrib.auth` is included in `INSTALLED_APPS`
2. Configure REST Framework permissions
3. Set login/logout redirect URLs

Copy the provided `settings.py` file to your project's `assignment` directory.

## Step 3: Create Template Files

Copy the following template files to their respective locations:

1. `myapp/templates/myapp/index.html` - Main country list page
2. `myapp/templates/registration/login.html` - Login page
3. `myapp/templates/registration/logged_out.html` - Logout confirmation page
4. `myapp/static/myapp/images/placeholder-flag.svg` - Placeholder flag image

## Step 4: Update URL Configuration

Update the URL configuration to include authentication URLs:

1. Copy the provided `myapp/urls.py` file
2. Copy the provided `assignment/urls.py` file

## Step 5: Update Views

Update your views to implement authentication requirements:

1. Copy the provided `myapp/views.py` file
2. Note the use of `LoginRequiredMixin` for class-based views
3. Note the use of `IsAuthenticated` permission class for API views

## Step 6: Create Management Command

Create a custom management command to easily add a test user:

1. Copy the provided init files to make the directories Python packages:
   - `myapp/management/__init__.py`
   - `myapp/management/commands/__init__.py`
2. Copy the `create_test_user.py` file to `myapp/management/commands/`

## Step 7: Run Migrations and Create User

Run migrations and create a test user:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py create_test_user
```

## Step 8: Test Authentication

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at http://localhost:8000/
   - You should be redirected to the login page
   - Login with username 'admin' and password 'password123'

3. Test API authentication:
   - Try accessing http://localhost:8000/api/countries/ directly in a new incognito browser window
   - You should be redirected to login
   - Test API authentication with curl:
     ```bash
     curl -u admin:password123 http://localhost:8000/api/countries/
     ```

## Step 9: Commit Your Changes

Once everything is working, commit your changes to version control:

```bash
git add .
git commit -m "Implement authentication and security features"
```

## Troubleshooting

If you encounter any issues:

1. Check the Django debug page for specific error messages
2. Verify that all required template files are in the correct locations
3. Make sure migrations have been applied
4. Check that the User model contains at least one user
5. Verify URL patterns are correctly defined