from django.contrib import admin


class StaffProfilesAdmin(admin.ModelAdmin):

    list_display = ("first_name", "last_name", "email", "designation", "contract_start", "contract_end")

    list_filter = ("deleted", )

    search_fields = ("staff__first_name", "staff__last_name", "staff__email", "designation")

    readonly_fields = ("id", "created_on", "updated_on")

    def first_name(self, instance):
        return instance.staff.first_name

    def last_name(self, instance):
        return instance.staff.last_name

    def email(self, instance):
        return instance.staff.email
