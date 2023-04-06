from django.db import models

from core.models import Base


class Events(Base):

    type = models.ForeignKey(to="competitions.EventTypes", on_delete=models.RESTRICT, null=False)

    start_on = models.DateTimeField()

    duration = models.DurationField()

    pool = models.ForeignKey(to="administration.Pools", on_delete=models.DO_NOTHING, null=True)

    gala = models.ForeignKey(to="competitions.Galas", on_delete=models.RESTRICT, null=False)

    participants = models.ManyToManyField(to="core.Users", through="competitions.Participation")
