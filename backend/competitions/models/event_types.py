from django.db import models
from django.db.models.functions import Lower


class EventTypes(models.Model):

    type = models.CharField(max_length=100, null=False, unique=True, primary_key=True)

    class Meta:

        verbose_name = "Event Type"

        verbose_name_plural = "Event Types"

        constraints = [
            models.UniqueConstraint(Lower('type'), name='unique_lower_gala_event_type')
        ]
