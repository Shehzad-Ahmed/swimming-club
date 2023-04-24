from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from competitions.models import Participation
from core import utils


class ParticipationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Participation

        fields = "__all__"

    def validate(self, attrs):
        requesting_user = self.context["request"].user
        if attrs["participant"].family != requesting_user.family:
            # In case a smart person adds participation on somebody else's behalf.
            raise ValidationError("You can not add participant outside of your family.")
        if not requesting_user.has_perm("competitions.add_participation") and attrs["participant"] == requesting_user:
            # In case Parent tries to participate.
            raise ValidationError("You are not allowed to participate.")
        if attrs["event"].start_on < utils.get_datetime():
            # In case someone tries to participate in old events.
            raise ValidationError("Can not participate in past events.")
        return attrs
