from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from .models import Noticia, Categoria
from django.core.paginator import Paginator

#dataNotation c#
# decorador para ver las noticias solamente como usuario logueado
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm





# Create your views here.


#def inicio (request):
 #   return HttpResponse("<h1>Hola mundo</h1> <h2> desde django</h2>")

#def inicio (request):
#   return render(request, 'noticias/inicio.html')

#dataNotation c#
# decorador para ver las noticias solamente como usuario logueado

def inicio(request):
    # obtener todas las noticias y mostrar en el inicio.html
    # ctx = {}
    # # clase.objetcs.all()==> select * from noticia
    # noticia = Noticia.objects.all()
    # ctx["noticias"] = noticia
    # return render(request, 'noticias/inicio.html', ctx)
    contexto = {}
    id_categoria = request.GET.get('id', None)

    if id_categoria:
        noticias = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        noticias = Noticia.objects.all()  # devolver una lista simil Tolist() c#

    paginator = Paginator(noticias, 3)  # Paginar las noticias, mostrando 10 noticias por página

    page_number = request.GET.get('page')
    noticias_paginadas = paginator.get_page(page_number)

    cat = Categoria.objects.all().order_by('nombre')

    contexto['noticias'] = noticias_paginadas
    contexto['categorias'] = cat

    return render(request, 'noticias/inicio.html', contexto)


@login_required
def Detalle_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    return render(request, 'noticias/detalle.html', contexto)

@login_required
def crear_noticia(request):
    
    data = {
        'form': NoticiaForm()
    }

    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('nombre_de_la_vista_exitosa')
            #return HttpResponse(('contactos/exito.html') + '?success=true')
            #return render(request,'noticias/exito.html')
            return redirect('listar_noticias')
        
    else:
        form = NoticiaForm()
    
    
    return render(request, 'noticias/crear_noticia.html', data)

@login_required
def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

@login_required
def ver_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)    
    return render(request, 'noticias/ver_noticia.html', {'noticia': noticia})

@login_required
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('ver_noticia', pk=pk)
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticias/editar_noticia.html', {'form': form})
@login_required
def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('listar_noticias')
    return render(request, 'noticias/eliminar_noticia.html', {'noticia': noticia})