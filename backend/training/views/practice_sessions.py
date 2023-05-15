from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from training.models import PracticeSessions
from training.serializers.practice_sessions import PracticeSessionsSerializer


class PracticeSessionsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = PracticeSessionsSerializer

    queryset = PracticeSessions.objects.all()

    permission_classes = (DjangoModelPermissions, )

    def get_queryset(self):
        return super().get_queryset().filter(
            squad__participants__family=self.request.user.family,
            deleted=False
        ).order_by(
            "-performance_uploaded",
            "start_at"
        )
