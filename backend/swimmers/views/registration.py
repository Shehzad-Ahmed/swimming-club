from rest_framework import viewsets

from swimmers.models import Families
from swimmers.serializers import RegistrationSerializer


class RegistrationViewSet(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin):

    serializer_class = RegistrationSerializer

    queryset = Families.objects.filter(deleted=False).all()
