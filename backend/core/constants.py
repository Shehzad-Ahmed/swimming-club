from django.db import models


class DifficultyLevelChoice(models.TextChoices):

    BEGINNER = "beginner", "Beginner"

    INTERMEDIATE = "intermediate", "Intermediate"

    ADVANCED = "advanced", "Advanced"

    ELITE = "elite", "Elite"
