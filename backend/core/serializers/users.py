from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

Users = get_user_model()


class UsersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Users

        fields = (
            "id",
            "created_on",
            "updated_on",
            "deleted",
            "first_name",
            "last_name",
            "email",
            "family",
            "date_of_birth",
            "password",
        )

        read_only_fields = (
            "id",
            "created_on",
            "updated_on",
            "deleted",
            "family",
        )


class UsersUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Users

        fields = (
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        )

    # def validate_date_of_birth(self, instance):
    #     if self.context["request"].user != instance and age():
    #


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['family'] = user.family.name
        return token
