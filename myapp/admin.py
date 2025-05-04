from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_common', 'cca3', 'region', 'capital', 'population')
    list_filter = ('region', 'subregion', 'independent', 'landlocked')
    search_fields = ('name_common', 'name_official', 'cca2', 'cca3', 'capital')
    ordering = ('name_common',)