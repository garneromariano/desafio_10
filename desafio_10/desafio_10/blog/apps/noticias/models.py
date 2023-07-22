from django.db import models
from django.conf import settings
import os #prueba

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150, default='Valor por defecto')
    cuerpo = models.TextField()
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='noticias/', null=True)
    categoria_noticia = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo
