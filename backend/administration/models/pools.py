from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Base


class Pools(Base):

    code = models.CharField(max_length=100, unique=True)

    length = models.FloatField(help_text=_("Pool length in meters"), null=False)

    depth = models.FloatField(help_text=_("Pool depth in meters"), null=False)

    available = models.BooleanField(default=True)

    last_service = models.DateTimeField(null=True)

    class Meta:

        verbose_name = "Swimming Pool"

        verbose_name_plural = "Swimming Pools"

    def __str__(self):
        return f"{self.code} - Available: {self.available}"

"""
Implement training screens.
Implement children details for parent.
Update profile screen.
Finalize permissions.
"""
