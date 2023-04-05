from django.db import models

from core.models import Base


class PracticeSessions(Base):

    start_at = models.DateTimeField(null=False)

    duration = models.DurationField(null=False)

    squad = models.ForeignKey(to="swimmers.Squads", null=True, on_delete=models.DO_NOTHING)

    pool = models.ForeignKey(to="administration.Pools", null=False, on_delete=models.DO_NOTHING)

    class Meta:

        verbose_name = "Practice Session"

        verbose_name_plural = "Practice Sessions"
