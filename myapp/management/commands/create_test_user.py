from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a test user'

    def handle(self, *args, **kwargs):
        username = 'testuser'
        password = 'testpass123'
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'User "{username}" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists.'))
