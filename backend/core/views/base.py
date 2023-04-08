from rest_framework import viewsets


class BaseGenericViewSet(viewsets.GenericViewSet):

    action_serializers = {}

    action_queryset = {}

    def get_serializer_class(self):
        """
        Looks for any particular Serializer based on action view set.
        """
        return self.action_serializers.get(
            self.action,
            self.action_serializers.get(
                "default",
                super().get_serializer_class()
            )
        )

    def get_queryset(self):
        """
        Looks for any particular Queryset based on action view set.
        """
        queryset_cls_name = self.action_queryset.get(
            self.action,
            self.action_queryset.get(
                "default",
                ""
            )
        )
        queryset_cls_getter = getattr(self, queryset_cls_name) if queryset_cls_name else super().get_queryset
        return queryset_cls_getter()
