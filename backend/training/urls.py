from django.urls import path, include
from rest_framework import routers

from training import views

router = routers.DefaultRouter()

router.register("performance", viewset=views.PerformanceViewSet, basename="performance")
router.register("practice-sessions", viewset=views.PracticeSessionsViewSet, basename="practice-sessions")

urlpatterns = [
    path("", include(router.urls))
]
