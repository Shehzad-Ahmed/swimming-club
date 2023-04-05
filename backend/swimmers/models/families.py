from django.db import models
from core.models import Base


class Families(Base):
    """
    Family model class. Signing up User will have a Families instance.
    """

    name = models.CharField(max_length=50, null=False)

    subscription = models.ForeignKey("swimmers.Subscriptions", null=True, on_delete=models.DO_NOTHING)

    class Meta:

        verbose_name = "Family"

        verbose_name_plural = "Families"
