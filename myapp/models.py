from django.db import models

class Country(models.Model):
    """
    Model representing a country with detailed information.
    """
    name = models.CharField(max_length=255, unique=True)
    alpha2code = models.CharField(max_length=2, unique=True)
    alpha3code = models.CharField(max_length=3, unique=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    subregion = models.CharField(max_length=255, null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    flag = models.URLField(max_length=500, null=True, blank=True)
    timezones = models.JSONField(default=list, null=True, blank=True)
    currencies = models.JSONField(default=list, null=True, blank=True)
    languages = models.JSONField(default=list, null=True, blank=True)
    borders = models.JSONField(default=list, null=True, blank=True)
    latlng = models.JSONField(default=list, null=True, blank=True)
    native_name = models.CharField(max_length=255, null=True, blank=True)
    numeric_code = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name