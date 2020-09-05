from django.db import models

# Create your models here.
class Programs(models.Model):
    diversity_program = models.CharField(max_length=100, null=True)
    diversity_link = models.CharField(max_length=100, null=True)
    diversity_industry = models.CharField(max_length=100, null=True)
    diversity_population = models.CharField(max_length=100, null=True)

class Internships(models.Model):
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
