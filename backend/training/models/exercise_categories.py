from django.db import models
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _


class ExerciseCategories(models.Model):
    """
    Model for Exercise Categories.
    The reason to keep this separate because the categories can be unique, so to avoid any discrepancy
    in filters being applied on Exercises in case of case mismatching in category.
    """

    category = models.CharField(max_length=100, unique=True, help_text=_(
        "indicate the category or type of exercise, such as 'strokes,' 'drills,' 'kick sets,' 'pull sets,' etc."
    ))

    class Meta:

        verbose_name = "Exercise Category"

        verbose_name_plural = "Exercise Categories"

        constraints = [
            models.UniqueConstraint(Lower('category'), name='unique_lower_exercise_category')
        ]
        # The unique constraint will avoid case mismatching.

    def __str__(self):
        return f"{self.category}"
