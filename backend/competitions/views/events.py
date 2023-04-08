from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from competitions.models import Events
from competitions.serializers.events import EventsReadOnlySerializer


class EventsViewSets(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventsReadOnlySerializer

    queryset = Events.objects.filter(deleted=False).all()

    permission_classes = (IsAuthenticated, )
