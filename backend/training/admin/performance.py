from django.contrib import admin
from django.contrib.auth import get_user_model

from training.models import PracticeSessions

Users = get_user_model()


class PerformanceAdmin(admin.ModelAdmin):

    list_display = ("swimmer_email", "started_at", "exercise_name", "squad_name")

    list_filter = ("repetitions", "distance", "pace", "intensity", "rest_frequency", "rest_length_avg")

    search_fields = ("swimmer__email", "session__exercise__name", "session__squad__name")

    ordering = ("-created_on", )

    readonly_fields = ("id", "created_on", "updated_on")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "swimmer":
            kwargs["queryset"] = Users.objects.filter(deleted=False, squads__isnull=False)

        if db_field.name == "session":
            kwargs["queryset"] = PracticeSessions.objects.filter(deleted=False, performance_uploaded=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def swimmer_email(self, instance):
        return instance.swimmer.email

    def started_at(self, instance):
        return instance.session.start_at

    def exercise_name(self, instance):
        return instance.session.exercise.name

    def squad_name(self, instance):
        return instance.session.squad.name
