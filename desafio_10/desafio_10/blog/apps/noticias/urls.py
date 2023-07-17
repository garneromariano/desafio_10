from django.urls import path
from . import views

app_name = 'noticias'

# URL de app noticias
urlpatterns = [
    path('',views.inicio,name='inicio'),
    
    # url para el detalle de la noticia por pk
    path('detalle<int:pk>', views.Detalle_Noticias, name='detalle')
    ]
