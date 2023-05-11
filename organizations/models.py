from django.db import models
# from event_app.models import User
# Create your models here.

class Organization(models.Model):
    name = models.CharField(unique=True, max_length = 50)
    bio = models.TextField()
    tickets_sold = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

