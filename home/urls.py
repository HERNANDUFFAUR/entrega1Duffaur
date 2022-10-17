from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    path('crear-persona/', views.crear_persona, name ='crear_persona'),
    path('busqueda-personas/', views.busqueda_personas, name ='busqueda_personas'),
    ]