import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_search.settings')
django.setup()

from search.models import Restaurant

csv_file_path = './restaurants_small.csv'

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Restaurant.objects.create(
            name=row['name'],
            location=row['location'],
            items=row['items'],
            lat_long=row['lat_long'],
            full_details=row['full_details']
        )
