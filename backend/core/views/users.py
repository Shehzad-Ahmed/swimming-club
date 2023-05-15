from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from core.serializers.users import UsersUpdateSerializer, UsersSerializer, UsersReadOnlySerializer
from core.views import BaseGenericViewSet

Users = get_user_model()


class UsersViewSet(BaseGenericViewSet,
                   viewsets.mixins.UpdateModelMixin,
                   viewsets.mixins.CreateModelMixin,
                   viewsets.mixins.ListModelMixin,
                   ):

    serializer_class = UsersUpdateSerializer

    queryset = Users.objects.all()

    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    action_serializers = {
        "create": UsersSerializer,
        "update": UsersUpdateSerializer,
        "list": UsersReadOnlySerializer,
    }

    action_queryset = {
        "default": "get_default_queryset",
        "list": "get_list_queryset",
    }

    def get_default_queryset(self):
        return self.queryset.filter(family=self.request.user.family).all()

    def get_list_queryset(self):
        return self.queryset.exclude(
            id=self.request.user.id
        ).filter(family=self.request.user.family, deleted=False).all()

    def create(self, request, *args, **kwargs):
        """
        API Endpoint to add swimmers in own family.
        """
        # Note: Subscription checks needs to be enforced in the future.
        request.data = {"family": request.user.family, **request.data}
        return super().create(request, *args, **kwargs)
