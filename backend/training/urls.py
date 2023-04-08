from django.urls import path, include
from rest_framework import routers

from training import views

router = routers.DefaultRouter()

router.register("performance", viewset=views.PerformanceViewSet, basename="performance")

urlpatterns = [
    path("", include(router.urls))
]
