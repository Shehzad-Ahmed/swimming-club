from django.contrib import admin


class ResultsAdmin(admin.ModelAdmin):

    list_display = ("gala_title", "event_type", "participant_email", "attended", "position", "score")

    list_editable = ("position", "score")

    search_fields = (
        "participation__event__type_id",
        "participation__participation__participant__email",
        "participation__event__gala__title"
    )

    readonly_fields = ("id", "created_on", "updated_on")

    @classmethod
    def gala_title(cls, instance):
        return instance.participation.event.gala.title

    @classmethod
    def event_type(cls, instance):
        return instance.participation.event.type_id

    @classmethod
    def participant_email(cls, instance):
        return instance.participation.participant.email
