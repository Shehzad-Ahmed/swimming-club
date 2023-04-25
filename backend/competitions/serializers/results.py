from rest_framework import serializers

from competitions.models import Results
from competitions.serializers import ResultsParticipationReadOnlySerializer
from core.serializers import UsersParticipantsReadOnlySerializer


class ResultsSerializer(serializers.ModelSerializer):

    details = ResultsParticipationReadOnlySerializer(read_only=True, source="participation")

    class Meta:

        model = Results

        fields = "__all__"

        read_only_fields = ("created_on", "updated_on", "id", "deleted")


class ScoreboardResultsReadOnlySerializer(serializers.Serializer):

    position = serializers.IntegerField()

    score = serializers.IntegerField()

    participant = serializers.SerializerMethodField()

    def get_participant(self, instance):
        return UsersParticipantsReadOnlySerializer(instance=instance.participation.participant).data
