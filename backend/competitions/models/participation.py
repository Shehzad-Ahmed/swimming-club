from django.db import models


class Participation(models.Model):
    """
    Model for participants.
    """

    event = models.ForeignKey(to="competitions.Events", on_delete=models.CASCADE, null=False)

    participant = models.ForeignKey(to="core.Users", on_delete=models.CASCADE, null=False)
