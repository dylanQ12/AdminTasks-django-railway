from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyectos_views, name='proyectos'),
    path('crear-proyecto/', views.crear_proyectos_views, name='crear-proyecto'),
    path('editar-proyecto/<int:id>/', views.editar_proyectos_views, name='editar-proyecto'),
    path('eliminar-proyecto/<int:id>/', views.eliminar_proyecto, name='eliminar-proyecto'),
]