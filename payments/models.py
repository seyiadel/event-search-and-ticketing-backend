from django.db import models
from ticket_app.models import Ticket

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