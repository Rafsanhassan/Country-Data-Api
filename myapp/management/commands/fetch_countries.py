import requests
from django.core.management.base import BaseCommand
from myapp.models import Country

class Command(BaseCommand):
    help = 'Fetch countries data from restcountries.com API and store in database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching countries data...')
        
        # Fetch data from API
        url = 'https://restcountries.com/v3.1/all'
        response = requests.get(url)
        
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {response.status_code}'))
            return
        
        countries_data = response.json()
        self.stdout.write(f'Successfully fetched {len(countries_data)} countries')
        
        # Clear existing data (optional)
        Country.objects.all().delete()
        self.stdout.write('Cleared existing countries data')
        
        # Process and save data
        counter = 0
        for country_data in countries_data:
            try:
                # Extract required fields
                name_common = country_data.get('name', {}).get('common', '')
                name_official = country_data.get('name', {}).get('official', '')
                cca2 = country_data.get('cca2', '')
                cca3 = country_data.get('cca3', '')
                flag_emoji = country_data.get('flag', '')
                flag_png = country_data.get('flags', {}).get('png', '')
                region = country_data.get('region', '')
                subregion = country_data.get('subregion', '')
                
                # Capital can be a list or missing
                capitals = country_data.get('capital', [])
                capital = capitals[0] if capitals else ''
                
                # Basic country attributes
                population = country_data.get('population', 0)
                area = country_data.get('area', 0)
                independent = country_data.get('independent', True)
                un_member = country_data.get('unMember', False)
                landlocked = country_data.get('landlocked', False)
                
                # More complex data structures
                currencies = country_data.get('currencies', {})
                languages = country_data.get('languages', {})
                latlng = country_data.get('latlng', [])
                borders = country_data.get('borders', [])
                timezones = country_data.get('timezones', [])
                
                # Create or update country record
                country, created = Country.objects.update_or_create(
                    cca3=cca3,
                    defaults={
                        'name_common': name_common,
                        'name_official': name_official,
                        'cca2': cca2,
                        'flag_emoji': flag_emoji,
                        'flag_png': flag_png,
                        'region': region,
                        'subregion': subregion,
                        'capital': capital,
                        'population': population,
                        'area': area,
                        'independent': independent,
                        'un_member': un_member,
                        'landlocked': landlocked,
                        'currencies': currencies,
                        'languages': languages,
                        'latlng': latlng,
                        'borders': borders,
                        'timezones': timezones,
                    }
                )
                
                counter += 1
                if counter % 50 == 0:
                    self.stdout.write(f'Processed {counter} countries')
                    
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing country {country_data.get("name", {}).get("common", "unknown")}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully processed {counter} countries'))