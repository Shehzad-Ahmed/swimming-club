
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import Base


class Profiles(Base):

    id = None

    user = models.OneToOneField(to="core.Users", on_delete=models.CASCADE, primary_key=True)

    skill_level = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(9, message="Skill level needs to be between 0 to 9")]
    )

    badge = models.CharField(max_length=50, default="", blank=True)

    overall_score = models.PositiveIntegerField(default=0)
