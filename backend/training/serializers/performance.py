from rest_framework import serializers

from training.models import Performance


class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Performance

        fields = "__all__"

        read_only_fields = ("created_on", "updated_on", "id")
