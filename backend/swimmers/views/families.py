from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from core.serializers.users import UsersSerializer


class FamiliesViewSet(viewsets.GenericViewSet):

    @action(methods=["post"], detail=False, url_path="add-member", url_name="add-member")
    def add_member(self, request, *args, **kwargs):

        if not self.request.user.has_perm("core.add_users"):
            return Response(status=403, data={"message": "You are not allowed to add user."})

        ser = UsersSerializer(data=request.data, context=self.get_serializer_context())
        ser.is_valid(raise_exception=True)
        ser.validated_data["family"] = self.request.user.family
        user = ser.save()
        return Response(status=200, data=UsersSerializer(instance=user).data)
