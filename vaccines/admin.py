# Admin
from django.contrib import admin

# Models
from models import Site, Event


class SiteAdmin(admin.ModelAdmin):
	list_filter = ('city',)


class EventAdmin(admin.ModelAdmin):
	list_display = ('date', 'site', 'hours_of_operation')
	list_filter = ('date', 'site',)
	date_hierarchy = 'date'


admin.site.register(Site, SiteAdmin)
admin.site.register(Event, EventAdmin)