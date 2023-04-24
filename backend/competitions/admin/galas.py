from django.contrib import admin


class GalasAdmin(admin.ModelAdmin):

    list_display = (
        "title", "start_on", "end_on"
    )

    list_editable = ("start_on", "end_on")

    search_fields = ("title",)

    readonly_fields = ("id", "created_on", "updated_on")
