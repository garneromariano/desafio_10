from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    asunto = models.CharField(max_length=40)
    texto = models.TextField()

    def __str__(self) -> str:
        return self.nombre
#