from django.db import models

from core.models import Base


class PracticeSessions(Base):

    start_at = models.DateTimeField(null=False)

    duration = models.DurationField(null=False)

    squad = models.ForeignKey(to="swimmers.Squads", null=True, on_delete=models.DO_NOTHING)

    pool = models.ForeignKey(to="administration.Pools", null=False, on_delete=models.DO_NOTHING)

    exercise = models.ForeignKey(to="training.exercises", null=False, on_delete=models.DO_NOTHING)

    performance_uploaded = models.BooleanField(default=False)

    class Meta:

        verbose_name = "Practice Session"

        verbose_name_plural = "Practice Sessions"

    def __str__(self):
        return f"{self.squad.name} - {self.start_at} - {self.exercise.name}"
