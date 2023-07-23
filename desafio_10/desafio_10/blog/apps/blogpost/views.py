
from django.shortcuts import render

from .forms import ComentarioForm
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django .http import HttpResponseRedirect


# # Create your views here.
# def inicio (request,post_id):
#     post= Post.objects.all()
#     return render(request,'blogpost/inicio.html',{'post':post})


def inicio(request):
    contexto = {}
    post= Post.objects.all()
    titulo_busqueda = request.GET.get('busqueda_titulo')
    
    if titulo_busqueda:
        post = post.filter(titulo__icontains=titulo_busqueda)

    
    post = post.order_by('-fechaCreado')

    paginator = Paginator(post, 3)  

    page_number = request.GET.get('page')
    post_paginadas = paginator.get_page(page_number)

    contexto['posteos'] = post_paginadas    
    #print(post_paginadas[0])

    #print(post)

    return render(request, 'blogpost/inicio.html', contexto)

def post_detalle(request,post_id):
    post = Post.objects.get(id=post_id) # est es el nombre que asignamos en urls para el id

    comentarios = post.comentario.filter(activo =True)

    if request.method == 'POST':
        form = ComentarioForm (request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # ponemos false para que solo guarde cuando el usuario de click al boton enviar, si no se va guardar solo antes que presione guardar
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect("")
    else:
        form = ComentarioForm   

    return render(request,'blogpost/post_detalle.html',{'post':post,'comentarios':comentarios,'form':form})