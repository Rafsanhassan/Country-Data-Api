from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import requests

from .models import Country
from .serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for countries that requires authentication.
    """
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]  # Require authentication for API access
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'cca2']

    @action(detail=True, methods=['get'])
    def regional_countries(self, request, pk=None):
        """
        Return countries in the same region as the specified country.
        """
        try:
            country = self.get_object()
            if not country.region:
                return Response({'detail': 'Country has no region specified'}, status=status.HTTP_404_NOT_FOUND)
                
            regional_countries = Country.objects.filter(region=country.region).exclude(id=country.id)
            serializer = self.get_serializer(regional_countries, many=True)
            return Response(serializer.data)
        except Country.DoesNotExist:
            return Response({'detail': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def languages(self, request, pk=None):
        """
        Return languages spoken in the specified country.
        """
        try:
            country = self.get_object()
            return Response(country.languages)
        except Country.DoesNotExist:
            return Response({'detail': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)


class CountryListView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the country list page.
    Requires authentication.
    """
    template_name = 'myapp/index.html'
    login_url = reverse_lazy('login')