from django.contrib import admin
from payments.models import Checkout, BankDetail
# Register your models here.

class BankDetailAdmin(admin.ModelAdmin):
    # date_hierarchy = "created_at"
    list_display = ['organization','account_number','bank_name', 'bank_code', 'account_name', 'recipient_code']
    list_filter = ['bank_name','owner__name']
    search_fields = ['account_number','account_name','owner__name']

    @admin.display()
    def organization(self, obj):
        return obj.owner.name


admin.site.register(BankDetail, BankDetailAdmin)

class CheckoutAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['event_name','status', 'quantity', 'user', 'ticket_type', 'amount', 'paystack_reference']
    list_filter = ['ticket__event__name','status', 'ticket__status',]
    search_fields = ['status','user','ticket__event__name']

    @admin.display(ordering="ticket__status")
    def ticket_type(self, obj):
        return obj.ticket.status

    @admin.display(ordering="ticket__event")
    def event_name(self, obj):
        return obj.ticket.event.name

admin.site.register(Checkout, CheckoutAdmin)