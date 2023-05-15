import uuid

from django.db import models
from django.db.models.functions import Lower

from core.constants import DifficultyLevelChoice


class Exercises(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.CharField(max_length=50, null=False, unique=True)

    category = models.ForeignKey(to="training.ExerciseCategories", null=False, on_delete=models.CASCADE)

    target_muscle = models.CharField(max_length=50, default="", null=False)

    difficulty_level = models.TextField(
        choices=DifficultyLevelChoice.choices, default=DifficultyLevelChoice.BEGINNER
    )

    recommended_duration = models.DurationField(null=True, default=None)

    recommended_repetitions = models.IntegerField(default=1)

    focus_area = models.CharField(max_length=100, default="")
    # would indicate the specific area of technique or form that the exercise type is designed to improve,
    # such as body position, arm movement, or kicking technique.

    iframe_video_link = models.URLField(null=True, default=None)

    class Meta:

        verbose_name = "Exercise"

        verbose_name_plural = "Exercises"

        constraints = [
            models.UniqueConstraint(Lower('name'), name='unique_lower_name_exercise')
        ]

    def __str__(self):
        return f"{self.name} - {self.category.category}"
