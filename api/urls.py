from rest_framework import routers
from api.views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"login", LoginViewset)
router.register(r"scraper", ScraperViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
