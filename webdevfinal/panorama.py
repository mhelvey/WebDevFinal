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
image.maps = 'https://www.google.com/maps/place/Ko+Olina+Golf+Club/@21.338169,-158.117906,17z/data=!4m6!1m3!3m2!1s0x7c0062c0ebaa227d:0x9e92e454d5a8b576!2sKo+Olina+Golf+Club!3m1!1s0x7c0062c0ebaa227d:0x9e92e454d5a8b576'
image.save()

image = hmod.Panorama.objects.get(title='hawaii2')
image.description = 'Hawaiian Coast'
image.maps = 'https://www.google.com/maps/place/Wailea+Beach+Marriott+Resort+%26+Spa/@20.687486,-156.443315,17z/data=!4m6!1m3!3m2!1s0x7954dada4b61da4d:0xe73f5d288a7aae5b!2sWailea+Beach+Marriott+Resort+%26+Spa!3m1!1s0x7954dada4b61da4d:0xe73f5d288a7aae5b'
image.save()

image = hmod.Panorama.objects.get(title='byutrack')
image.description = 'BYU track'
image.maps = 'https://www.google.com/maps/place/Track+and+Field+Complex/@40.2538014,-111.6552664,17z/data=!4m6!1m3!3m2!1s0x874d90bc4aa0b68d:0xbf3eb3a3f30fdc4c!2sBrigham+Young+University!3m1!1s0x0000000000000000:0x98bdb2cbfa225065'
image.save()

image = hmod.Panorama.objects.get(title='volley')
image.description = 'Smith Fieldhouse'
image.maps = 'https://www.google.com/maps/place/Department+of+Exercise+Sciences/@40.2478954,-111.6546629,18z/data=!4m2!3m1!1s0x0000000000000000:0xfb6baaef49b36811'
image.save()

image = hmod.Panorama.objects.get(title='wyoming1')
image.description = 'Fremont Lake, WY'
image.maps = 'https://www.google.com/maps/place/Fremont+Lake,+Wyoming/@42.9611995,-109.8065211,12z/data=!4m2!3m1!1s0x8757ed29e09677ed:0x3a2ea2683182c914'
image.save()

image = hmod.Panorama.objects.get(title='wyoming2')
image.description = 'Half Moon Lake, WY'
image.maps = 'https://www.google.com/maps/place/Half+Moon+Lake,+Wyoming+82941/@42.9242625,-109.7390287,14z/data=!3m1!4b1!4m2!3m1!1s0x87578d9922c7d3b7:0xe481f1d3de3c01c2'
image.save()

image = hmod.Panorama.objects.get(title='paris2')
image.description = 'Paris from Arc de Triomphe'
image.maps = 'https://www.google.com/maps/place/Arc+de+Triomphe/@48.873792,2.295028,17z/data=!3m1!4b1!4m2!3m1!1s0x47e66fec70fb1d8f:0xd9b5676e112e643d'
image.save()

image = hmod.Panorama.objects.get(title='paris3')
image.description = 'Musée du Louvre'
image.maps = 'https://www.google.com/maps/place/Louvre+Pyramid/@48.8608086,2.3356162,17z/data=!4m7!1m4!3m3!1s0x47e671d877937b0f:0xb975fcfa192f84d4!2sLouvre+Museum!3b1!3m1!1s0x0000000000000000:0xb0088e1f7c07f451'
image.save()

image = hmod.Panorama.objects.get(title='powell')
image.description = 'Houseboat in Lake Powell'
image.maps = 'https://www.google.com/maps/place/Lake+Powell,+UT+86040/@36.9388458,-111.4847167,15z/data=!3m1!4b1!4m2!3m1!1s0x8739d46fcc1d6c6b:0x409adb24f99ef4f5'
image.save()

image = hmod.Panorama.objects.get(title='powell2')
image.description = 'Lake Powell'
image.maps = 'https://www.google.com/maps/place/Lake+Powell,+UT+86040/@36.9388458,-111.4847167,15z/data=!3m1!4b1!4m2!3m1!1s0x8739d46fcc1d6c6b:0x409adb24f99ef4f5'
image.save()

image = hmod.Panorama.objects.get(title='beach')
image.description = 'Carmel Beach, CA'
image.maps = 'https://www.google.com/maps/place/Carmel+Beach,+Carmel-By-The-Sea,+CA+93923/@36.5502383,-121.9291215,15z/data=!3m1!4b1!4m2!3m1!1s0x808de63ebf5b219f:0x223e49989e2c65a6'
image.save()