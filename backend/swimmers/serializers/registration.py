

"""
Serializers for registration process.
"""
from django.db import transaction
from rest_framework import serializers

from core.serializers.users import UsersSerializer
from swimmers.models import Families


class RegistrationSerializer(serializers.ModelSerializer):

    family_name = serializers.CharField(source="name")

    class Meta:

        model = Families

        exclude = ("status", "verified_on", "name")

        read_only_fields = ("id", "created_on", "updated_on", "deleted", "created_by")

    def create(self, validated_data):
        users = self.initial_data.pop("users")

        with transaction.atomic():
            family = Families(**validated_data)
            ser = UsersSerializer(data=users)
            ser.is_valid(raise_exception=True)
            ser.validated_data["family"] = family
            user = ser.save()
            family.created_by = user
            family.save(update_fields=("created_by", ))
        return family
