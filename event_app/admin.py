from django.contrib import admin
from event_app.models import User, EventInfo

admin.site.register(User)

class EventInfoAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['name','location','country','created_at','organizer','earnings', 'start_date','end_date']
    list_filter = ['name','location', 'country', 'start_date','end_date','organizer__name']
    search_fields = ['name','organizer__name','location','country']
    
    @admin.display()
    def organizer(self, obj):
        return obj.organizer.name
admin.site.register(EventInfo, EventInfoAdmin)