from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Country
from .serializers import CountrySerializer, CountryDetailSerializer

def index(request):
    """View for the web interface."""
    return render(request, 'myapp/index.html')

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for countries that allows CRUD operations.
    
    list:
    Return a list of all countries.
    
    retrieve:
    Return details of a specific country.
    
    create:
    Create a new country entry.
    
    update:
    Update an existing country's details.
    
    destroy:
    Delete an existing country.
    """
    queryset = Country.objects.all().order_by('name')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['region', 'subregion', 'alpha2code', 'alpha3code']
    search_fields = ['name', 'alpha2code', 'alpha3code', 'capital']
    ordering_fields = ['name', 'population', 'area']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CountryDetailSerializer
        return CountrySerializer

    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        """List all countries in the same region as the specified country."""
        country = self.get_object()
        same_region_countries = Country.objects.filter(region=country.region).exclude(id=country.id)
        serializer = CountrySerializer(same_region_countries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_language(self, request):
        """List countries that speak a specified language."""
        language = request.query_params.get('language', None)
        if language is None:
            return Response(
                {"error": "Language parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Filter countries where the specified language is in the languages field
        # This implementation assumes languages are stored as a JSON array of language codes or names
        # Adjust the query based on how languages are stored in your model
        countries = Country.objects.filter(languages__icontains=language)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search for countries by name with partial matching."""
        query = request.query_params.get('name', None)
        if query is None:
            return Response(
                {"error": "Name parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        countries = Country.objects.filter(name__icontains=query)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)