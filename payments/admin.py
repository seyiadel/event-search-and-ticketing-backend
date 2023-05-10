from django.contrib import admin
from payments.models import Checkout
# Register your models here.


class CheckoutAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['event_name','status', 'quantity', 'user', 'ticket_type']
    list_filter = ['ticket__event','status', 'ticket__status',]
    search_fields = ['status','user']

    @admin.display(ordering="ticket__status")
    def ticket_type(self, obj):
        return obj.ticket.status

    @admin.display(ordering="ticket__event")
    def event_name(self, obj):
        return obj.ticket.event.name

admin.site.register(Checkout, CheckoutAdmin)