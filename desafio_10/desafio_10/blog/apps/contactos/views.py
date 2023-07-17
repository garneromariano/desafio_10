from django.shortcuts import render

# Create your views here.
#def contactos (request):
#    return render(request, 'contactos/contacto2.html')
from .forms import ContactoForm
# decorador para ver las noticias solamente como usuario logueado
from django.contrib.auth.decorators import login_required

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        ContactoForm(data=request.POST).save()

    return render(request, 'contactos/formulario.html', data)
