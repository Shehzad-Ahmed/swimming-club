from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions

from competitions.models import Results
from competitions.serializers import ResultsSerializer, ScoreboardResultsReadOnlySerializer
from core.views import BaseGenericViewSet


class CustomFiltersBackend(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        # queryset = queryset.filter(participation__participant__family=request.user.family)
        return super().filter_queryset(request, queryset, view)


class ResultsViewSet(BaseGenericViewSet, viewsets.ReadOnlyModelViewSet):

    serializer_class = ResultsSerializer

    queryset = Results.objects.filter(deleted=False, participation__event__results_published=True)

    permission_classes = (DjangoModelPermissions, )

    filter_backends = (CustomFiltersBackend, filters.SearchFilter, filters.OrderingFilter)

    filterset_fields = ("position", "attended", "participation__event")

    search_fields = ("note", )

    ordering_fields = ("created_on", "position", "score", "attended")

    action_serializers = {
        "scoreboard": ScoreboardResultsReadOnlySerializer,
    }

    action_queryset = {
        "default": "get_default_queryset",
        "scoreboard": "",
    }

    def get_default_queryset(self):
        return self.queryset.filter(participation__participant__family=self.request.user.family)

    def get_scoreboard_queryset(self):
        return self.queryset.all()

    @action(methods=["GET"], detail=False, name="scoreboard")
    def scoreboard(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
