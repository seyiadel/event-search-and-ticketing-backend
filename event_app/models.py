from django.db import models
from django.contrib.auth.models import AbstractUser
from event_app.managers import UserManager
from organizations.models import Organization
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=67,)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['date_joined',]


EVENT_TYPE = [
    ("Paid", "Paid"),
    ("Free", "Free"),
]

class EventInfo(models.Model):
    name = models.TextField()
    description = models.TextField()
    artwork = models.ImageField(null=True)
    venue = models.TextField()
    type = models.CharField(choices=EVENT_TYPE, max_length=40)
    location = models.CharField(default="Lagos", max_length=32)
    country = models.CharField(default="Nigeria", max_length=32)
    start_time = models.TimeField()
    start_date = models.DateField()
    end_time = models.TimeField()
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')
    earnings = models.IntegerField(null=True)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['created_at',]

