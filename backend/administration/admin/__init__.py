from django.contrib import admin

from administration.admin.plans import PlansAdmin
from administration.admin.pools import PoolsAdmin
from administration.models import Plans, Pools

admin.site.register(Plans, PlansAdmin)
admin.site.register(Pools, PoolsAdmin)
