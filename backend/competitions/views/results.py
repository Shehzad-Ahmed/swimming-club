from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from competitions.models import Results
from competitions.serializers import ResultsSerializer


class ResultsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ResultsSerializer

    queryset = Results.objects.filter(deleted=False)

    permission_classes = (IsAuthenticated, DjangoModelPermissions)
