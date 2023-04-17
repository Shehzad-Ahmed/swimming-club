from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core import constants

from swimmers.models import Families


class FamiliesMixinSerializer:

    @classmethod
    def validate_name(cls, name):
        if name.lower() in constants.FAMILY_NAME_BLACKLIST:
            raise ValidationError(f"Family name: {name} not allowed")
        return name


class FamiliesSerializer(FamiliesMixinSerializer, serializers.ModelSerializer):

    class Meta:

        model = Families

        fields = ("name",)

