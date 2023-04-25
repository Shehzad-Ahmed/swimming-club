from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from competitions.models import Events
from competitions.serializers import EventsReadOnlySerializer
from core import utils


class EventsViewSets(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventsReadOnlySerializer

    queryset = Events.objects.filter(deleted=False, results_published=False).all()

    # This permission class allows anonymous users to see events.
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    def get_queryset(self):
        # Can only see events starting ahead.
        return super().get_queryset().filter(start_on__gt=utils.get_datetime())
