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


new = hmod.Panorama.objects.get(title='byutrack')
print(new.filename)