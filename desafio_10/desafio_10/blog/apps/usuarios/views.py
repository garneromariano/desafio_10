from django.shortcuts import render

# Create your views here.
# importts
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistroForm


class Registro(CreateView):
    # forms django
    form_class = RegistroForm
    success_url = reverse_lazy('login') #especifica la URL a la que se redirigirá después de que se haya creado exitosamente el objeto. En este caso, se establece como 'login', que es un nombre de URL registrado en EL archivo de URLs
    template_name = 'usuarios/registro.html' # es un atributo de la clase CreateView que especifica la plantilla HTML que se utilizará para renderizar la página de creación del objeto. En este caso, se establece como 'usuarios/registro.html', lo que significa que la plantilla se buscará en la carpeta usuarios dentro de la carpeta de TEMPLATES.
