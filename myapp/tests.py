from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Country

class CountryModelTests(TestCase):
    def test_create_country(self):
        country = Country.objects.create(
            name_common='Test Country',
            name_official='Republic of Test',
            cca2='TC',
            cca3='TCY',
            region='Test Region',
            population=1000000
        )
        self.assertEqual(country.name_common, 'Test Country')
        self.assertEqual(country.region, 'Test Region')
        self.assertEqual(str(country), 'Test Country')

class APITests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        
        # Create test country
        self.country = Country.objects.create(
            name_common='Test Country',
            name_official='Republic of Test',
            cca2='TC',
            cca3='TCY',
            region='Test Region',
            population=1000000
        )
        
        # Setup API client
        self.client = APIClient()
    
    def test_countries_list_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('country-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_countries_list_unauthenticated(self):
        response = self.client.get(reverse('country-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_country_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('country-detail', args=[self.country.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_common'], 'Test Country')