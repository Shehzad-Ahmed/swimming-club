from django.db import models

from core.models import Base


class BillingPeriods(models.TextChoices):

    DAILY = "daily", "Daily"
    WEEKLY = "weekly", "Weekly"
    MONTHLY = "monthly", "Monthly"
    YEARLY = "yearly", "Yearly"


class Plans(Base):

    name = models.CharField(max_length=50, unique=True, null=False)

    description = models.TextField(default="", null=False)

    price = models.FloatField(null=False)

    billing_period = models.CharField(choices=BillingPeriods.choices, null=False, max_length=20)

    features = models.JSONField(default={})
    