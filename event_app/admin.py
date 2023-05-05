from django.contrib import admin
from event_app.models import User, Event
# Register your models here.

admin.site.register(User)
admin.site.register(Event)