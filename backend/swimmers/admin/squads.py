from django.contrib import admin


class SquadsAdmin(admin.ModelAdmin):

    list_display = ("name", "minimum_age", "maximum_age", "skill_level")

    list_filter = ("minimum_age", "maximum_age", "skill_level")

    search_fields = ("name", "participants__email")

    ordering = ("skill_level", )

    readonly_fields = ("id", "created_on", "updated_on")
