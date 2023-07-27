from rest_framework import serializers
from api.models import LoginModel, ScraperListModel


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "password")
        model = LoginModel

class RegisterSerializerPost(serializers.ModelSerializer):
    class Meta:
        exclude = ("id",)
        model = LoginModel
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("password","id")
        model = LoginModel

class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ScraperListModel
