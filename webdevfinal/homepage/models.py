from django.db import models

# Create your models here.
class Panorama(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.TextField(max_length=500)
    file_path = models.TextField(max_length=500)
    mime_type = models.TextField(max_length=25)
    title = models.TextField(max_length=40)
    description = models.TextField(null=True, max_length=400)