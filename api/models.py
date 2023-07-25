from django.db import models
import uuid

# Create your models here.

class LoginModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class ScraperListModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name_scraper = models.CharField(max_length=255)
    url = models.TextField()
    account = models.ForeignKey(LoginModel, on_delete=models.CASCADE)
    last_run = models.DateField(auto_now=True)
    status = models.CharField(max_length=10)