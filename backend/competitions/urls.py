from django.urls import path, include
from rest_framework import routers

from competitions import views

router = routers.DefaultRouter()

router.register("results", viewset=views.ResultsViewSet, basename="results")
router.register("galas", viewset=views.GalasViewSet, basename="galas")
router.register("events/participation", viewset=views.ParticipationViewSet, basename="events-participation")
router.register("events", viewset=views.EventsViewSets, basename="events")

urlpatterns = [
    path("", include(router.urls))
]
