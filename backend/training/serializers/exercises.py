from rest_framework import serializers

from training.models import Exercises


class ExercisesSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:

        model = Exercises

        fields = "__all__"

        read_only_fields = ("id", )

    def get_category(self, instance):
        return instance.category.category
