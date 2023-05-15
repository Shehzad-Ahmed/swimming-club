from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from training.models import Performance
from training.serializers import PerformanceSerializer


class PerformanceViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = PerformanceSerializer

    queryset = Performance.objects.filter(deleted=False)

    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = (DjangoFilterBackend, )

    filterset_fields = ("session", )

    def get_queryset(self):
        return super().get_queryset().filter(swimmer__family=self.request.user.family)
