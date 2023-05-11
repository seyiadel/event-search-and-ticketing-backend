from django.db import models
from event_app.models import EventInfo

# Create your models here.
class Ticket(models.Model):
    status = models.CharField(default="Regular", max_length= 34)
    created_at = models.DateTimeField(auto_now_add = True)
    price = models.IntegerField()
    available_tickets = models.IntegerField()
    event = models.ForeignKey(EventInfo, on_delete=models.DO_NOTHING, related_name="tickets")
    start_time = models.TimeField()
    start_date = models.DateField()
    end_time = models.TimeField()
    end_date = models.DateField()
    total_checkout_amount = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.event.name} {self.status}"
