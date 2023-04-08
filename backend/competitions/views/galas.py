from rest_framework import viewsets

from competitions.models import Galas
from competitions.serializers import GalasReadOnlySerializer


class GalasViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GalasReadOnlySerializer

    queryset = Galas.objects.filter(deleted=False).all()
