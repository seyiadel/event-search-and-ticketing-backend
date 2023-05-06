from django.db import models
from event_app.models import Event, User
# Create your models here.
class Ticket(model.Model):
    event = models.OneToOneField(Event,)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    buyer = models.OneToOneField(User,)

    @property
    def total_price(self):
        return self.event.price * self.quantity

    def __str__(self):
        return self.event.name
