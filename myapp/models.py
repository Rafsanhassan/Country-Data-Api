from django.db import models

class Country(models.Model):
    """Model to store country data"""
    name_common = models.CharField(max_length=255)
    name_official = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=2, unique=True)  # ISO 3166-1 alpha-2 code
    cca3 = models.CharField(max_length=3, unique=True)  # ISO 3166-1 alpha-3 code
    flag_emoji = models.CharField(max_length=10, null=True, blank=True)
    flag_png = models.URLField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    population = models.BigIntegerField(default=0)
    area = models.FloatField(null=True, blank=True)
    independent = models.BooleanField(default=True)
    un_member = models.BooleanField(default=True)
    landlocked = models.BooleanField(default=False)
    currencies = models.JSONField(null=True, blank=True)
    languages = models.JSONField(null=True, blank=True)
    latlng = models.JSONField(null=True, blank=True)  # [latitude, longitude]
    borders = models.JSONField(null=True, blank=True)  # List of border country codes
    timezones = models.JSONField(null=True, blank=True)  # List of timezones
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name_common']
    
    def __str__(self):
        return self.name_common
