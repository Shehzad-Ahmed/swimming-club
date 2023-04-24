from django.db import models


class Participation(models.Model):
    """
    Model for participants.
    """

    event = models.ForeignKey(to="competitions.Events", on_delete=models.CASCADE, null=False)

    participant = models.ForeignKey(to="core.Users", on_delete=models.CASCADE, null=False)

    class Meta:

        unique_together = (("event", "participant"),)

    def __str__(self):
        return f"{self.event.gala.title}-{self.event.type_id}-{self.participant.email}"
