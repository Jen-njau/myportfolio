from __future__ import unicode_literals
from django.db import models

class contactme(models.Model):
    name=models.CharField(max_length=30,blank="false")
    email=models.EmailField()
    subject=models.CharField(max_length=50,blank="false")
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name