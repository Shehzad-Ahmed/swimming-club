from django.contrib import admin

from training.admin.exercise_categories import ExerciseCategoriesAdmin
from training.admin.exercises import ExercisesAdmin
from training.admin.performance import PerformanceAdmin
from training.admin.practice_sessions import PracticeSessionsAdmin
from training.models import ExerciseCategories, Exercises, Performance, PracticeSessions

admin.site.register(ExerciseCategories, admin_class=ExerciseCategoriesAdmin)
admin.site.register(Exercises, admin_class=ExercisesAdmin)
admin.site.register(Performance, admin_class=PerformanceAdmin)
admin.site.register(PracticeSessions, admin_class=PracticeSessionsAdmin)
