from django.db import models

# Create your models here.
class Usertable(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.username)