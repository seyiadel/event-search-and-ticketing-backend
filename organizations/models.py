from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(unique=True, max_length = 50)
    bio = models.TextField()
    tickets_sold = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('event_app.User', on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f"{self.name}"

