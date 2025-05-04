from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    # Web views
    path('', views.index, name='index'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api/regions/', views.get_regions, name='regions'),
    path('api/search/', views.search_countries, name='search'),
    path('api/country/<str:code>/', views.get_country_by_code, name='country-detail'),
]