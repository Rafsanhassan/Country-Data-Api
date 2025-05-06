from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Include our app's URLs
    path('', include('myapp.urls')),
    
    # DRF authentication for browsable API
    path('api-auth/', include('rest_framework.urls')),
]