from django.contrib import admin
from payments.models import Checkout, BankDetail, WithdrawEventEarning, ListOfBank
# Register your models here.

admin.site.register(ListOfBank)

class WithdrawEventEarningAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['organization','event_name','event_earning','bank_name','account_name','account_number', 'reference_codes', 'status']
    list_filter = ['status','event__name', 'bank_detail__bank_name']
    search_fields = ['reference_code','status','event__name', 'event__organizer__name']

    @admin.display()
    def event_name(self, obj):
        return obj.event.name

    @admin.display()
    def organization(self, obj):
        return obj.event.organizer

    @admin.display()
    def event_earning(self,obj):
        return obj.event.earnings

    @admin.display()
    def bank_name(self,obj):
        return obj.bank_detail.bank_name

    @admin.display()
    def account_name(self,obj):
        return obj.bank_detail.account_name
 
    @admin.display()
    def account_number(self,obj):
        return obj.bank_detail.account_number

    @admin.display()
    def reference_codes(self,obj):
        return obj.reference_code
    

admin.site.register(WithdrawEventEarning, WithdrawEventEarningAdmin)

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