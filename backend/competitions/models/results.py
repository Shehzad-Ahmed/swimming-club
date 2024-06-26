from django.db import models

from core.models import Base


class Results(Base):

    participation = models.ForeignKey(to="competitions.Participation", on_delete=models.RESTRICT, null=False)

    attended = models.BooleanField(default=True)

    score = models.FloatField(default=0)

    position = models.PositiveIntegerField(default=0)

    # Depending on the event type a record note will be added.
    record = models.TextField()

    class Meta:
        verbose_name = "Result"

        verbose_name_plural = "Results"
