from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.functions import Lower

from core.models import Base


class Squads(Base):
    """
    Squad of swimmers.
    """

    supervisor = models.ForeignKey(
        to="administration.StaffProfiles", null=True, on_delete=models.RESTRICT, default=None, blank=True
    )

    name = models.CharField(max_length=100, null=False, unique=True)

    minimum_age = models.IntegerField(default=3)

    maximum_age = models.IntegerField(null=False)
    # minimum and maximum age decides the age group.

    participants = models.ManyToManyField("core.Users")

    skill_level = models.PositiveIntegerField(
        validators=[MaxValueValidator(9, message="Skill level needs to be between 0 to 9")]
    )

    class Meta:

        verbose_name = "Squad"

        verbose_name_plural = "Squads"

        constraints = [
            models.UniqueConstraint(Lower('name'), name='unique_lower_name_squad')
        ]

    def __str__(self):
        return f"{self.name} - {self.skill_level}"
