from django.db import models

from core.models import Base


class Galas(Base):

    title = models.TextField()

    about = models.TextField()

    start_on = models.DateTimeField(null=False)

    end_on = models.DateTimeField(null=False)

    class Meta:
        verbose_name = "Gala"

        verbose_name_plural = "Galas"
