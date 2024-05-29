from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='usuarios'),
    path('crear-usuario/', views.crear_usuarios, name='crear-usuario'),
    path('editar-usuario/<int:id>/', views.editar_usuarios, name='editar-usuario'),
    path('crear-usuario/<int:id>/', views.crear_usuarios, name='eliminar-usuario'),
    path('perfil/<int:id>', views.ver_perfil, name='ver-perfil'),
]