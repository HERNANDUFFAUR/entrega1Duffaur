from django.urls import path
from avanzado import views

urlpatterns = [
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/crear', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id>', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:id>', views.eliminar_mascota, name='eliminar_mascota')
]
