from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename='country')

urlpatterns = [
    # Web interface URL
    path('', views.index, name='index'),
    
    # API URLs
    path('api/', include(router.urls)),
]