from django.db import models

from core.models import Base


class PerformanceIntensity(models.TextChoices):

    LOW = "low", "Low"
    MODERATE = "moderate", "Moderate"
    HIGH = "high", "High"


class Performance(Base):
    """
    Model for recording performance of swimmer.
    """

    session = models.ForeignKey(to="training.PracticeSessions", on_delete=models.DO_NOTHING, null=False)

    swimmer = models.ForeignKey(to="core.Users", on_delete=models.CASCADE, null=False)

    repetitions = models.IntegerField(default=1)

    duration = models.DurationField()

    distance = models.FloatField(null=True)
    # If applicable.

    pace = models.IntegerField(null=True)

    intensity = models.CharField(choices=PerformanceIntensity.choices, max_length=20)

    rest_frequency = models.IntegerField(default=0)

    rest_length_avg = models.DurationField(null=True)

    heart_rate = models.IntegerField(null=True)

    technique = models.TextField(default="", null=False, blank=True)

    goal = models.TextField(default="", null=False, blank=True)

    feedback = models.TextField(default="", null=False, blank=True)

