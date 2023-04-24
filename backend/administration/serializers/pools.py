from rest_framework import serializers


class PoolsReadOnlySerializer(serializers.Serializer):

    id = serializers.UUIDField()

    code = serializers.CharField()

    length = serializers.IntegerField()

    depth = serializers.IntegerField()
