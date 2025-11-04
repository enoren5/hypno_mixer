from django.db import models

# Create your models here.

class AuthToggle(models.Model):
    email = models.EmailField(max_length=50, default='')
    linkedin = models.CharField(max_length=50, default='')

    def __str__(self):
        return "Options"