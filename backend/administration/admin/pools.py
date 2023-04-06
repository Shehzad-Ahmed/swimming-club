from django.contrib import admin


class PoolsAdmin(admin.ModelAdmin):

    list_display = ("code", "length", "depth", "available", "last_service")

    list_filter = ("available", "deleted")

    search_fields = ("code", "length", "depth")

    readonly_fields = ("id", "created_on", "updated_on")
