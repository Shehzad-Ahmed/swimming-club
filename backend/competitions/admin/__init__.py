from django.contrib import admin

from competitions.admin.event_types import EventTypesAdmin
from competitions.admin.events import EventsAdmin
from competitions.admin.galas import GalasAdmin
from competitions.admin.results import ResultsAdmin
from competitions.models import EventTypes, Galas, Events, Results

admin.site.register(EventTypes, admin_class=EventTypesAdmin)
admin.site.register(Galas, admin_class=GalasAdmin)
admin.site.register(Events, admin_class=EventsAdmin)
admin.site.register(Results, admin_class=ResultsAdmin)
