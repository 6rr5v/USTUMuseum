from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    fields = ['title_event', 'announcement_event', 'picture_event', 'date_event']


admin.site.register(Event, EventAdmin)
