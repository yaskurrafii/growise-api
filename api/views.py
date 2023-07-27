from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import LoginSerializer, RegisterSerializer,RegisterSerializerPost, ScraperSerializer
from api.models import LoginModel, ScraperListModel

# Create your views here.

class RegisterViewset(ModelViewSet):
    serializer_class = {"create" : RegisterSerializerPost, "default" : RegisterSerializer}
    queryset = LoginModel.objects.all()

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'create':
            return self.serializer_class['create']
        return self.serializer_class['default']

class LoginViewset(ModelViewSet):
    serializer_class = LoginSerializer
    queryset = LoginModel.objects.all()


class ScraperViewset(ModelViewSet):
    serializer_class = ScraperSerializer
    queryset = ScraperListModel.objects.all()