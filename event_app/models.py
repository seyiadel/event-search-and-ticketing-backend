from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.TextField()
    description = models.TextField()
    artwork = models.ImageField()
    venue = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = 'created_at'
