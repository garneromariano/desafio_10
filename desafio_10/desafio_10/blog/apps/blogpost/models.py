from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtituloGenral = models.CharField(max_length=255, null=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cuerpo=models.TextField()
    slug = models.SlugField()
    fechaCreado= models.DateTimeField(auto_now_add=True,null=True)
    titulo2 = models.CharField(max_length=255, null=True)
    subtituloGenral2 = models.CharField(max_length=255, null=True)
    cuerpo2 = models.TextField( null=True)
    imagen1 = models.ImageField(upload_to='blogpost/', null=True)
    imagen2 = models.ImageField(upload_to='blogpost/', null=True)
    pieDeFoto = models.CharField(max_length=255,null=True)
    pieDePosteo=models.TextField(null=True)
    # def __str__(self):
    #      return  "post de " + ' | ' + self.autor +  ' | ' +  self.titulo
    def __str__(self):  # metodo  Tostring() 
     return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comentario')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fechaCreado = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    activo=models.BooleanField(default=False)
    def __str__(self):
        return  "comentario de " + ' | ' + self.nombre +  ' | ' +  self.contenido
       # return f"comentario de {nombre} {contenido}"