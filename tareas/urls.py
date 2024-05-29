from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='tareas'),
    path('crear-tareas/', views.crear_tareas, name='crear-tarea'),
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar-tarea'),
    path('eliminar-tarea/<int:tarea_id>/', views.eliminar_tarea, name='eliminar-tarea'),
]