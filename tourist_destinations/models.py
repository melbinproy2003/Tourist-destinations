from django.db import models
from guestapp.models import Usertable

class Destination(models.Model):
    name = models.CharField(max_length=100)
    weather = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField()
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField()
    by = models.ForeignKey(Usertable, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
