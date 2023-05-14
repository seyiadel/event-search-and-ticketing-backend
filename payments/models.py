from django.db import models
from ticket_app.models import Ticket
from organizations.models import Organization
from event_app.models import EventInfo
import uuid

# Create your models here.
class Checkout(models.Model):
    user = models.EmailField()
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING, related_name='checkouts')
    quantity = models.IntegerField()
    paystack_reference = models.CharField(max_length=65, blank=True)
    amount = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=8, blank=True)
    created_at =models.DateTimeField(auto_now_add= True)

    @property
    def total_price(self):
        return self.ticket.price * self.quantity

    def __str__(self):
        return f"{self.ticket.event.name}"

class BankDetail(models.Model):
    account_number = models.IntegerField()
    bank_name = models.CharField(max_length= 20, blank=True)
    bank_code = models.IntegerField()
    account_name = models.CharField(max_length= 50, blank=True)
    recipient_code = models.CharField(max_length= 45, blank=True)
    owner = models.OneToOneField(Organization, on_delete=models.CASCADE, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.bank_name} {self.account_number} - {self.owner.name}"

class WithdrawEventEarning(models.Model):
    event = models.OneToOneField(EventInfo, on_delete=models.CASCADE)
    bank_detail = models.ForeignKey(BankDetail, on_delete=models.DO_NOTHING)
    reference_code = models.UUIDField(uuid.uuid4, max_length = 45, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Pending", max_length=24)
    
    def __str__(self):
        return f"{self.event.name}, {self.reference_code}"