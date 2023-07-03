from django.contrib import admin
from ticket_app.models import Ticket
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['uuid','event','organization','status','price', 'available_tickets','total_checkout_amount','start_date', 'end_date']
    list_filter = ['event__name','start_date','status']
    search_fields = ['status','event__name','event__organizer__name']
    
    @admin.display()
    def event(self, obj):
        return obj.event.name

    @admin.display()
    def organization(self, obj):
        return obj.event.organizer.name

admin.site.register(Ticket, TicketAdmin)
