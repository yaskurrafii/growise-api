from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import LoginSerializerPost, LoginSerializerList, ScraperSerializer
from api.models import LoginModel, ScraperListModel

# Create your views here.

class LoginViewset(ModelViewSet):
    serializer_class = {"create" : LoginSerializerPost, "default" : LoginSerializerList} 
    queryset = LoginModel.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action.lower() == 'create':
            return self.serializer_class[self.action]
        return self.serializer_class['default']


class ScraperViewset(ModelViewSet):
    serializer_class = ScraperSerializer
    queryset = ScraperListModel.objects.all()