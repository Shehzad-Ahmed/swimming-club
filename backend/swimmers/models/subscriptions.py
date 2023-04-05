from django.db import models

from core.models import Base


class Subscriptions(Base):

    start_at = models.DateTimeField(null=False)

    end_at = models.DateTimeField(null=False)

    plan = models.ForeignKey("administration.Plans", null=False, on_delete=models.CASCADE)

    class Meta:

        verbose_name = "Subscription"

        verbose_name_plural = "Subscriptions"
