from django.contrib import admin


class EventTypesAdmin(admin.ModelAdmin):

    list_display = ("type", )

    search_fields = ("type", )
