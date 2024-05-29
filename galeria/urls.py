from django.urls import path
from . import views

urlpatterns = [
    # Sección de Albúm.
    path("", views.listar_albums, name="galeria"),
    path("crear/", views.crear_album, name="crear-album"),
    path("album/<int:id>/editar/", views.editar_album, name="editar-album"),
    path("album/<int:id>/eliminar/", views.eliminar_album, name="eliminar-album"),
    # Sección de Albúm/Fotos
    path("album/<int:id>/fotos/", views.ver_fotos, name="ver-fotos"),
    path("album/<int:id>/subir-foto/", views.subir_foto, name="subir-foto"),
    path("album/<int:id>/editar-foto/", views.editar_foto, name="editar-foto"),
    path("album/<int:id>/eliminar-foto/", views.eliminar_foto, name="eliminar-foto")
]
