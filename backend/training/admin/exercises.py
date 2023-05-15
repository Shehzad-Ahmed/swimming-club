from django.contrib import admin


class ExercisesAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "difficulty_level",
        "recommended_duration",
        "focus_area",
    )

    list_editable = ("difficulty_level", "recommended_duration")

    list_filter = ("category", "difficulty_level", "target_muscle")

    search_fields = ("name", "category__category", "focus_area")

    readonly_fields = ("id", )

    list_display_links = ("name", )
