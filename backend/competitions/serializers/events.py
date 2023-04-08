from rest_framework import serializers

from competitions.serializers import GalasReadOnlySerializer


class EventsReadOnlySerializer(serializers.Serializer):

    type = serializers.CharField()

    start_on = serializers.DateTimeField()

    duration = serializers.DurationField()

    pool = serializers.SlugRelatedField(slug_field="code")

    gala = GalasReadOnlySerializer()
