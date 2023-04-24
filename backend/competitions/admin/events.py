from django.contrib import admin


class EventsAdmin(admin.ModelAdmin):

    list_display = (
        "type", "gala_title", "skill_level", "start_on", "duration", "pool",
    )

    readonly_fields = ("id", "created_on", "updated_on")

    list_editable = ("start_on", "duration", "skill_level")

    search_fields = ("gala__title", "type")

    def gala_title(self, instance):
        return instance.gala.title

    def _type(self, instance):
        return instance._type.type
