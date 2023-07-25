from rest_framework import serializers
from api.models import LoginModel, ScraperListModel


class LoginSerializerPost(serializers.ModelSerializer):
    class Meta:
        exclude = ("id",)
        model = LoginModel
class LoginSerializerList(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LoginModel

class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ScraperListModel
