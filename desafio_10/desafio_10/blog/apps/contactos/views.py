from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

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
    '''
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        ContactoForm(data=request.POST).save()

    return render(request, 'contactos/formulario.html', data)
    '''
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('nombre_de_la_vista_exitosa')
            #return HttpResponse(('contactos/exito.html') + '?success=true')
            return render(request,'contactos/exito.html')
    else:
        form = ContactoForm()

    #return render(request, 'nombre_de_la_plantilla.html', {'form': form})
    return render(request, 'contactos/formulario.html', data)