from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Base


class Pools(Base):

    code = models.CharField(max_length=100, unique=True)

    length = models.FloatField(help_text=_("Pool length in meters"), null=False)

    depth = models.FloatField(help_text=_("Pool depth in meters"), null=False)

    available = models.BooleanField(default=True)

    last_service = models.DateTimeField(null=True)
