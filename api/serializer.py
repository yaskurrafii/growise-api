from rest_framework import serializers
from api.models import LoginModel


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LoginModel
