from django.urls import path
from .views import *
from . import views

app_name = 'noticias'

# URL de app noticias
urlpatterns = [
   


    path('', views.inicio, name='inicio'),
    path('detalle/<int:pk>/', views.Detalle_Noticias, name='detalle'),  # Agrega una barra antes de <int:pk>
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),  # Asegúrate de tener una barra después de crear_noticia
    path('listar/', views.listar_noticias, name='listar_noticias'),
    path('<int:pk>/', views.ver_noticia, name='ver_noticia'),
    path('<int:pk>/editar/', views.editar_noticia, name='editar_noticia'),
    path('<int:pk>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
    ]

    

