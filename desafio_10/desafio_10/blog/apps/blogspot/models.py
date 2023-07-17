from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cuerpo=models.TextField()

def __str__(self):
    return self.titulo + ' | ' + self.autor 