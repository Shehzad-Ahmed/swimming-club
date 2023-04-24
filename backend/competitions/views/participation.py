from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from competitions.models import Participation
from competitions.serializers import ParticipationSerializer


class ParticipationViewSet(
    viewsets.ReadOnlyModelViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin
):

    # Only permitted users will manipulate participation.
    permission_classes = (DjangoModelPermissions,)

    queryset = Participation.objects.all()

    serializer_class = ParticipationSerializer

    def get_queryset(self):
        # This will ensure only members from same family will be able to add/delete participation.
        return super().get_queryset().filter(
            participant__family=self.request.user.family,
            event__deleted=False,
            participant__deleted=False,
        )
