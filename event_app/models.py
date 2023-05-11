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


class EventInfo(models.Model):
    name = models.TextField()
    description = models.TextField()
    artwork = models.ImageField(null=True)
    venue = models.TextField()
    location = models.CharField(default="Lagos", max_length=32)
    country = models.CharField(default="Nigeria", max_length=32)
    time = models.TimeField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['created_at',]

