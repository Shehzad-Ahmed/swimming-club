from django.contrib import admin


class PracticeSessionsAdmin(admin.ModelAdmin):

    list_display = ("start_at", "squad_name", "performance_uploaded", "pool_code", "exercise_name", "duration")

    list_editable = ("duration", "performance_uploaded")

    list_filter = ("pool__code", )

    search_fields = ("squad__name", "pool__code", "exercise__name")

    ordering = ("-start_at", )

    def squad_name(self, instance):
        return instance.squad.name

    def pool_code(self, instance):
        return instance.pool.code

    def exercise_name(self, instance):
        return instance.exercise.name
