from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings


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

    @classmethod
    def validate_password(cls, password):
        validate_password(password)
        return password


class UsersUpdateSerializer(serializers.ModelSerializer):

    family_name = serializers.CharField(required=False)

    class Meta:

        model = Users

        fields = (
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "family_name",
        )

    def update(self, instance, validated_data):
        family_name = validated_data.pop("family_name", None)
        with transaction.atomic():
            data = super().update(instance, validated_data)
            from swimmers.serializers import FamiliesSerializer
            family_ser = FamiliesSerializer(instance=instance.family, data={"name": family_name})
            family_ser.is_valid(raise_exception=True)
            family_ser.save()
        return data

    # def validate_date_of_birth(self, instance):
    #     if self.context["request"].user != instance and age():
    #


class UserData:

    @classmethod
    def get_user_data(cls, user):
        data = dict()
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['email'] = user.email
        data['family'] = user.family.name
        data['role'] = user.groups.values_list("name", flat=True).first()
        data['squad'] = user.squads_set.values_list("name", flat=True).first()
        return data


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token.payload.update(UserData.get_user_data(user))
        return token

class UserTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])
        # Inject users updated data.
        refresh.payload.update(UserData.get_user_data(Users.objects.get(id=refresh["user_id"])))
        data = {"access": str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh"] = str(refresh)

        return data


class UsersParticipantsReadOnlySerializer(serializers.Serializer):

    first_name = serializers.CharField()

    last_name = serializers.CharField()
