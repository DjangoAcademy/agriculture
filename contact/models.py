
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    message = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.email
