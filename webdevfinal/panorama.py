#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'webdevfinal.settings'
import django
django.setup()

# import models and run django/python commands
from homepage import models as hmod

names = [
         'hawaii',
         'hawaii2',
         'byutrack',
         'volley',
         'wyoming1',
         'wyoming2',
         'paris2',
         'paris3',
         'powell',
         'powell2',
         'beach',

         ]

for name in names:
    try:
        image = hmod.Panorama.objects.get(title=name)
        print("Image " + image.title + " already exists")
    except hmod.Panorama.DoesNotExist:
        image = hmod.Panorama()
        image.title = name
        image.filename = image.title + ".jpg"
        image.file_path = "images/" + image.filename
        image.mime_type = "image/jpg"
        image.save()
        print("Image " + image.title + " created")

image = hmod.Panorama.objects.get(title='hawaii')
image.description = 'Ko Olina Beach'
image.save()

image = hmod.Panorama.objects.get(title='hawaii2')
image.description = 'Hawaiian Coast'
image.save()

image = hmod.Panorama.objects.get(title='byutrack')
image.description = 'BYU track'
image.save()

image = hmod.Panorama.objects.get(title='volley')
image.description = 'Smith Fieldhouse'
image.save()

image = hmod.Panorama.objects.get(title='wyoming1')
image.description = 'Fremont Lake, WY'
image.save()

image = hmod.Panorama.objects.get(title='wyoming2')
image.description = 'Half Moon Lake, WY'
image.save()

image = hmod.Panorama.objects.get(title='paris2')
image.description = 'Paris from Arc de Triomphe'
image.save()

image = hmod.Panorama.objects.get(title='paris3')
image.description = 'Musée du Louvre'
image.save()

image = hmod.Panorama.objects.get(title='powell')
image.description = 'Houseboat in Lake Powell'
image.save()

image = hmod.Panorama.objects.get(title='powell2')
image.description = 'Lake Powell'
image.save()

image = hmod.Panorama.objects.get(title='beach')
image.description = 'Carmel Beach, CA'
image.save()