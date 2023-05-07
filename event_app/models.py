from django.db import models
from django.contrib.auth.models import AbstractUser
from event_app.managers import UserManager
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


class Organizer(models.Model):
    name = models.CharField(max_length=54)
    bio = models.TextField(null=True)

class EventInfo(models.Model):
    name = models.TextField()
    description = models.TextField()
    artwork = models.ImageField()
    venue = models.TextField()
    location = models.CharField(default="Lagos", max_length=32)
    country = models.CharField(default="Nigeria", max_length=32)
    time = models.TimeField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['created_at',]

