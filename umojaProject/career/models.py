from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    content = RichTextField()
