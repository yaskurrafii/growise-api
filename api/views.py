from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import LoginSerializer
from api.models import LoginModel

# Create your views here.

class LoginViewset(ModelViewSet):
    serializer_class = LoginSerializer
    queryset = LoginModel.objects.all()