from django.urls import path, include
from rest_framework import routers

from swimmers import views
router = routers.DefaultRouter()

router.register("register", viewset=views.RegistrationViewSet)
router.register("families", viewset=views.FamiliesViewSet, basename="families")


urlpatterns = [
    path("", include(router.urls))
]
