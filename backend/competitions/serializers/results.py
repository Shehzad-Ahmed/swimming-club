from rest_framework import serializers

from competitions.models import Results


class ResultsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Results

        fields = "__all__"

        read_only_fields = ("created_on", "updated_on", "id", "deleted")
