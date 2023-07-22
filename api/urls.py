from rest_framework import routers
from api.views import *

router = routers.SimpleRouter()
router.register(r"login", LoginViewset)

urlpatterns = router.urls
