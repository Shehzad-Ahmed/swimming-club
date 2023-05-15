from django.contrib import admin

from swimmers.admin.squads import SquadsAdmin
from swimmers.models import Squads

admin.site.register(Squads, admin_class=SquadsAdmin)
