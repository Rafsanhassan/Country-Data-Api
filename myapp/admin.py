from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'alpha3code', 'capital', 'region', 'population')
    list_filter = ('region', 'subregion')
    search_fields = ('name', 'alpha2code', 'alpha3code', 'capital')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'native_name', 'alpha2code', 'alpha3code', 'numeric_code')
        }),
        ('Location', {
            'fields': ('capital', 'region', 'subregion', 'latlng')
        }),
        ('Demographics & Geography', {
            'fields': ('population', 'area', 'borders')
        }),
        ('Additional Information', {
            'fields': ('currencies', 'languages', 'timezones', 'flag')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )