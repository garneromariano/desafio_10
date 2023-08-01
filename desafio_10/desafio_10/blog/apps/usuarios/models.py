from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    facebook = models.CharField(max_length=100,  null=True, blank=True)
    whatsapp = models.CharField(max_length=100,  null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True,  blank=True)
    pass