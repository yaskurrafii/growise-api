from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializer import (
    LoginSerializer,
    RegisterSerializer,
    RegisterSerializerPost,
    ScraperSerializer,
)
from api.models import LoginModel, ScraperListModel
from rest_framework.response import Response

# Create your views here.


class RegisterViewset(ModelViewSet):
    serializer_class = {"create": RegisterSerializerPost, "default": RegisterSerializer}
    queryset = LoginModel.objects.all()

    def create(self, request, *args, **kwargs):
        user = LoginModel.objects.filter(
            username=request.data["username"], email=request.data["email"]
        )
        if len(user) != 0:
            return Response({"error": "username or email have been used"}, status=401)
        return super().create(request, *args, **kwargs)

    def get_serializer_class(self):
        print(self.action)
        if self.action == "create":
            return self.serializer_class["create"]
        return self.serializer_class["default"]


class LoginViewset(ModelViewSet):
    serializer_class = LoginSerializer
    queryset = LoginModel.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        user = LoginModel.objects.get(username=data["username"])
        if user.password != data["password"]:
            return Response({"description": False})
        return Response({"description": True})


class ScraperViewset(ModelViewSet):
    serializer_class = ScraperSerializer
    queryset = ScraperListModel.objects.all()
