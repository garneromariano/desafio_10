from django.shortcuts import render,redirect,get_list_or_404

# Create your views here.
# importts
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistroForm

from django.contrib.auth.models import User
from django.contrib.auth import login 

class Registro(CreateView):
    # forms django
    form_class = RegistroForm
    success_url = reverse_lazy('inicio2') #especifica la URL a la que se redirigirá después de que se haya creado exitosamente el objeto. En este caso, se establece como 'login', que es un nombre de URL registrado en EL archivo de URLs
    template_name = 'usuarios/registro.html' # es un atributo de la clase CreateView que especifica la plantilla HTML que se utilizará para renderizar la página de creación del objeto. En este caso, se establece como 'usuarios/registro.html', lo que significa que la plantilla se buscará en la carpeta usuarios dentro de la carpeta de TEMPLATES.

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        #agregamo la imagen
        if 'imagen' in self.request.FILES:
            user.imagen = self.request.FILES['imagen']
            user.save()
            
        login(self.request, user)  # Iniciar sesión automáticamente después del registro exitoso
        return response