from django.urls import path, include
from rest_framework import routers

from swimmers import views
router = routers.DefaultRouter()

router.register("register", viewset=views.RegistrationViewSet)


urlpatterns = [
    path("", include(router.urls))
]
