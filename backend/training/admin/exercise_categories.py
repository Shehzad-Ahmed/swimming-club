from django.contrib import admin


class ExerciseCategoriesAdmin(admin.ModelAdmin):

    list_display = ("category",)

    list_filter = ("category",)

    search_fields = ("category",)

    readonly_fields = ("id", )

    list_display_links = ("category", )
