from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Country
from .serializers import CountrySerializer, CountryListSerializer, CountryDetailSerializer

# Web views
@login_required
def index(request):
    """Render the home page with countries data"""
    countries_count = Country.objects.count()
    regions = Country.objects.values_list('region', flat=True).distinct()
    context = {
        'countries_count': countries_count,
        'regions': regions,
    }
    return render(request, 'myapp/index.html', context)

# API views
class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing countries
    """
    queryset = Country.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name_common', 'name_official', 'capital', 'region', 'subregion']
    ordering_fields = ['name_common', 'population', 'area']
    filterset_fields = ['region', 'subregion', 'independent', 'landlocked']
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CountryListSerializer
        return CountryDetailSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_regions(request):
    """
    API endpoint to get unique regions
    """
    regions = Country.objects.values_list('region', flat=True).distinct()
    regions = [region for region in regions if region]  # Filter out None/empty values
    return Response(sorted(regions))

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def search_countries(request):
    """
    API endpoint to search countries by term
    """
    search_term = request.query_params.get('q', '')
    if not search_term:
        return Response({'error': 'Search term is required'}, status=400)
    
    countries = Country.objects.filter(name_common__icontains=search_term)
    serializer = CountryListSerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_country_by_code(request, code):
    """
    API endpoint to get a country by its code (cca2 or cca3)
    """
    try:
        if len(code) == 2:
            country = Country.objects.get(cca2__iexact=code)
        else:
            country = Country.objects.get(cca3__iexact=code)
        
        serializer = CountryDetailSerializer(country)
        return Response(serializer.data)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=404)