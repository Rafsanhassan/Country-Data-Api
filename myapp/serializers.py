from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    """Serializer for the Country model with all fields"""
    class Meta:
        model = Country
        fields = '__all__'

class CountryListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing countries"""
    class Meta:
        model = Country
        fields = ['id', 'name_common', 'cca3', 'flag_emoji', 'region']

class CountryDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for a single country"""
    class Meta:
        model = Country
        fields = [
            'id', 'name_common', 'name_official', 'cca2', 'cca3',
            'flag_emoji', 'flag_png', 'region', 'subregion',
            'capital', 'population', 'area', 'independent',
            'un_member', 'landlocked', 'currencies', 'languages',
            'latlng', 'borders', 'timezones'
        ]