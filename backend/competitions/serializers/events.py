from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from competitions.serializers import GalasReadOnlySerializer
from administration.serializers import PoolsReadOnlySerializer
from core.serializers import UsersParticipantsReadOnlySerializer


class EventsReadOnlySerializer(serializers.Serializer):

    id = serializers.UUIDField()

    type = serializers.CharField(source="type_id")

    start_on = serializers.DateTimeField()

    duration = serializers.DurationField()

    pool = PoolsReadOnlySerializer()

    gala = GalasReadOnlySerializer()

    skill_level = serializers.IntegerField()

    participation_id = serializers.SerializerMethodField()

    participants = UsersParticipantsReadOnlySerializer(many=True)

    def get_participation_id(self, instance):
        request = self.context["request"]
        try:
            return instance.participation_set.get(participant=request.user.id).id
        except ObjectDoesNotExist:
            return None


class EventsParticipationReadOnlySerializer(EventsReadOnlySerializer):

    participation_id = None

    participants = None

    pool = None
