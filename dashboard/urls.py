from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.dashboardView, name='dashboard'),
    path('todas-mis-tareas/', views.lista_todas_tareas_usuario, name='mis-tareas'),
    path('tareas-pendientes/', views.tareas_pendientes, name='tareas-pendientes')
]