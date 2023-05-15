from django.core.validators import MaxValueValidator
from django.db import models

from core.models import Base


class Events(Base):

    type = models.ForeignKey(to="competitions.EventTypes", on_delete=models.RESTRICT, null=False)

    start_on = models.DateTimeField()

    duration = models.DurationField()

    pool = models.ForeignKey(to="administration.Pools", on_delete=models.DO_NOTHING, null=True)

    gala = models.ForeignKey(to="competitions.Galas", on_delete=models.RESTRICT, null=False)

    participants = models.ManyToManyField(to="core.Users", through="competitions.Participation")

    skill_level = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(9, message="Skill level needs to be between 0 to 9")]
    )

    results_published = models.BooleanField(default=False)

    class Meta:

        verbose_name = "Event"

        verbose_name_plural = "Events"
