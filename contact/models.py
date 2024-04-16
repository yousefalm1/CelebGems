from django.contrib.auth.models import User
from django.db import models


class contactMessage(models.Model):
    Name = models.CharField(max_length= 100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
