from django.contrib import admin


class PlansAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "price", "billing_period")

    list_filter = ("billing_period", "deleted", "price")

    search_fields = ("name", "description", "features")

    list_editable = ("price", "billing_period")

    readonly_fields = ("created_on", "updated_on", "id")
