from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    descrption = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
