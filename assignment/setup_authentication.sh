#!/bin/bash
# Script to set up authentication for the Country Data Explorer project

echo "Setting up authentication for Country Data Explorer..."

# Create necessary directories for templates
echo "Creating directory structure..."
mkdir -p myapp/templates/registration
mkdir -p myapp/management/commands

# Copy template files
echo "Setting up template files..."
# Note: You should manually copy the template files created in this implementation

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create a test user
echo "Creating test user..."
python manage.py create_test_user

echo "Authentication setup complete!"
echo ""
echo "You can now run the server with:"
echo "python manage.py runserver"
echo ""
echo "Access the application at http://localhost:8000/"
echo "Login with username 'admin' and password 'password123'"