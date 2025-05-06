from django.urls import path, include
from rest_framework import routers
from . import views

# Create a router for our API views
router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
    
    # Front-end URLs
    path('', views.CountryListView.as_view(), name='country_list'),
]