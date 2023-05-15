from rest_framework import serializers

from training.serializers import ExercisesSerializer


class PracticeSessionsSerializer(serializers.Serializer):

    id = serializers.UUIDField()

    start_at = serializers.DateTimeField()

    duration = serializers.DurationField()

    squad = serializers.CharField()

    pool_code = serializers.SerializerMethodField()

    exercise = ExercisesSerializer()

    performance_uploaded = serializers.BooleanField()

    def get_pool_code(self, instance):
        return instance.pool.code
