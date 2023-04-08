from rest_framework import serializers


class GalasReadOnlySerializer(serializers.Serializer):

    id = serializers.UUIDField()

    created_on = serializers.DateTimeField()

    updated_on = serializers.DateTimeField()

    title = serializers.CharField()

    about = serializers.CharField()

    start_on = serializers.DateTimeField()

    end_on = serializers.DateTimeField()
