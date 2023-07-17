from django.urls import path
from . import views

app_name = 'blogspot'

# URL de app noticias
urlpatterns = [
    path('',views.blogspot,name='blogspot')
    ]
