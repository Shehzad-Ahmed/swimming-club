from django.db import models


class Participants(models.Model):
    """
    Model for participants.
    """

    event = models.ForeignKey(to="competitions.Galas", on_delete=models.CASCADE, null=False)

    participant = models.ForeignKey(to="core.Users", on_delete=models.CASCADE, null=False)
