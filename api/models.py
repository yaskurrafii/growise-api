from django.db import models

# Create your models here.

class LoginModel(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class ScraperListModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name_scraper = models.CharField(max_length=255)