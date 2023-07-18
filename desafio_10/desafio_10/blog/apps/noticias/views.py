from django.shortcuts import render, HttpResponse
from .models import Noticia, Categoria
from django.core.paginator import Paginator

#dataNotation c#
# decorador para ver las noticias solamente como usuario logueado
from django.contrib.auth.decorators import login_required





# Create your views here.


#def inicio (request):
 #   return HttpResponse("<h1>Hola mundo</h1> <h2> desde django</h2>")

#def inicio (request):
#   return render(request, 'noticias/inicio.html')

#dataNotation c#
# decorador para ver las noticias solamente como usuario logueado
@login_required
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
