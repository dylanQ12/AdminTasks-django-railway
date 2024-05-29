from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album, Foto

"""
   Sección de Fotos
   Vistas de Albúm/Fotos
"""


@login_required
def crear_album(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("desc")

        if titulo and descripcion:
            album = Album(titulo=titulo, descripcion=descripcion, usuario=request.user)
            album.save()
            messages.success(request, '¡Álbum creado correctamente!')
            return redirect("galeria")
    return render(request, "crear-album.html")


@login_required
def editar_album(request, id):
    album = get_object_or_404(Album, pk=id)

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("desc")

        if titulo and descripcion:
            album.titulo = titulo
            album.descripcion = descripcion
            album.save()
            messages.success(request, '¡Álbum actualizado correctamente!')
            return redirect("galeria")

    return render(request, "editar-album.html", {"album": album})


@login_required
def ver_fotos(request, id):
    album = get_object_or_404(Album, pk=id, usuario=request.user)
    fotos = album.fotos.all()
    return render(request, "ver-fotos.html", {"album": album, "fotos": fotos})


@login_required
def subir_foto(request, id):
    album = get_object_or_404(Album, pk=id, usuario=request.user)

    if request.method == "POST":
        foto = request.FILES.get("foto")
        descripcion = request.POST.get("desc")

        nueva_foto = Foto.objects.create(
            album=album, imagen=foto, descripcion=descripcion
        )
        messages.success(request, '¡Foto subida con éxito!')
        return redirect("ver-fotos", id=album.id)
    return render(request, "subir-foto.html", {"album": album})


@login_required
def editar_foto(request, id):
    foto = get_object_or_404(Foto, pk=id, album__usuario=request.user)
    album = foto.album

    if request.method == "POST":
        nueva_foto = request.FILES.get("foto")
        nueva_descripcion = request.POST.get("desc")

        if foto and nueva_descripcion:
            foto.imagen = nueva_foto
            foto.descripcion = nueva_descripcion
            foto.save()
            messages.success(request, '¡Foto actualizada con éxito!')
            return redirect("ver-fotos", id=album.id)

    return render(request, "editar-foto.html", {"album": album, "foto": foto})


@login_required
def eliminar_foto(request, id):
    foto = get_object_or_404(Foto, pk=id, album__usuario=request.user)
    album = foto.album

    if request.method == "POST":
        foto.delete()
        messages.success(request, '¡Foto eliminada con éxito!')
        return redirect("ver-fotos", id=album.id)

    return render(request, "ver-fotos", {"album": album, "foto": foto})


@login_required
def listar_albums(request):
    albums = Album.objects.filter(usuario=request.user).prefetch_related("fotos")
    return render(request, "list-album.html", {"albums": albums})


@login_required
def eliminar_album(request, id):
    album = get_object_or_404(Album, pk=id, usuario=request.user)
    if request.method == "POST":
        album.delete()
        messages.success(request, "¡Álbum eliminado correctamente!")
        return redirect("galeria")
    return render(request, "list-album.html", {"album": album})
