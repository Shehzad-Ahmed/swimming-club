

"""
Serializers for registration process.
"""
from django.contrib.auth.models import Group
from django.core.exceptions import BadRequest
from django.db import transaction
from rest_framework import serializers

from core import utils
from core.serializers.users import UsersSerializer
from swimmers.models import Families
from swimmers.models.profiles import Profiles


class RegistrationSerializer(serializers.ModelSerializer):

    family_name = serializers.CharField(source="name")

    parent = serializers.BooleanField(required=False)

    class Meta:

        model = Families

        exclude = ("status", "verified_on", "name")

        read_only_fields = ("id", "created_on", "updated_on", "deleted", "created_by")

    def create(self, validated_data):
        users = self.initial_data.pop("users")
        parent = self.validated_data.pop("parent", False)
        with transaction.atomic():
            family = Families(**validated_data)
            ser = UsersSerializer(data=users)
            ser.is_valid(raise_exception=True)
            ser.validated_data["family"] = family
            user = ser.save()
            if parent:
                user.groups.set(Group.objects.filter(name="Parents"))
            else:
                self.validate_adult_swimmer_age(user)
                Profiles.objects.create(user=user)
                user.groups.set(Group.objects.filter(name="Adult Swimmers"))
            family.created_by = user
            family.save(update_fields=("created_by", ))
        return family

    @classmethod
    def validate_adult_swimmer_age(cls, user):
        if utils.age(user.date_of_birth) < 18:
            BadRequest("User must be 18 years old.")
