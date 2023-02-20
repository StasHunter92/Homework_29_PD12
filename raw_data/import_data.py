import csv
import os

import django
from django.apps import apps

from Homework_29_PD12.settings import BASE_DIR

CAT_PATH = os.path.join(BASE_DIR, 'raw_data', 'category.csv')
LOC_PATH = os.path.join(BASE_DIR, 'raw_data', 'location.csv')
US_PATH = os.path.join(BASE_DIR, 'raw_data', 'user.csv')
ADS_PATH = os.path.join(BASE_DIR, 'raw_data', 'ad.csv')
US_LOC_PATH = os.path.join(BASE_DIR, 'raw_data', 'user_location.csv')

# ----------------------------------------------------------------------------------------------------------------------
# Setup env settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Homework_29_PD12.settings')
django.setup()

# ----------------------------------------------------------------------------------------------------------------------
# Add models
Category = apps.get_model('ads', 'Category')
Location = apps.get_model('users', 'Location')
User = apps.get_model('users', 'User')
Advertisement = apps.get_model('ads', 'Advertisement')

# ----------------------------------------------------------------------------------------------------------------------
# Write data from file to database
with open(CAT_PATH, encoding="utf-8") as f:
    data = csv.DictReader(f)

    for row in data:
        Category.objects.create(name=row.get('name'))

# ----------------------------------------------------------------------------------------------------------------------
# Write data from file to database
with open(LOC_PATH, encoding="utf-8") as f:
    data = csv.DictReader(f)

    for row in data:
        location = {
            "name": row.get('name'),
            "lat": row.get('lat'),
            "lng": row.get('lng')
        }

        Location.objects.create(**location)

# ----------------------------------------------------------------------------------------------------------------------
# Write data from file to database
with open(US_PATH, encoding="utf-8") as f:
    data = csv.DictReader(f)

    for row in data:
        data = {"first_name": row.get('first_name'),
                "last_name": row.get('last_name'),
                "username": row.get('username'),
                "password": row.get('password'),
                "role": row.get('role'),
                "age": row.get('age'),
                }
        User.objects.create(**data)

# ----------------------------------------------------------------------------------------------------------------------
# Write data from file to database
with open(ADS_PATH, encoding="utf-8") as f:
    data = csv.DictReader(f)

    for row in data:
        is_published = True if row.get('is_published') == "TRUE" else False
        data = {"name": row.get('name'),
                "author_id": row.get('author_id'),
                "price": row.get('price'),
                "description": row.get('description'),
                "is_published": is_published,
                "image": row.get('image'),
                "category_id": row.get('category_id'),
                }

        Advertisement.objects.create(**data)

# ----------------------------------------------------------------------------------------------------------------------
# Success message
print("Success")
