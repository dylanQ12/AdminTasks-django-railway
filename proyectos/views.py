from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Proyecto


# Create your views here.
@login_required
def lista_proyectos_views(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    data = {"proyectos": proyectos}
    return render(request, "list-proyectos.html", data)


@login_required
def crear_proyectos_views(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("desc")

        if titulo and descripcion:
            proyecto = Proyecto(
                titulo=titulo, descripcion=descripcion, usuario=request.user
            )
            proyecto.save()
            messages.success(request, "¡Proyecto creado correctamente!")
            return redirect(reverse("proyectos"))
        else:
            messages.error(request, "No se pudo crear el proyecto")

    return render(request, "crear-proyecto.html")


def editar_proyectos_views(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("desc")
        if titulo and descripcion:
            proyecto.titulo = titulo
            proyecto.descripcion = descripcion
            proyecto.save()
            messages.success(request, "¡Proyecto actualizado correctamente!")
            return redirect(reverse("proyectos"))
        else:
            messages.error(request, "No se pudo actualizar el proyecto")

    return render(request, "editar-proyecto.html", {"proyecto": proyecto})


@login_required
def eliminar_proyecto(request, id):
    if request.method == "POST":
        proyecto = get_object_or_404(
            Proyecto, pk=id, usuario=request.user
        )  # Asegura que sólo se usa pk para buscar
        proyecto.delete()
        messages.success(request, "¡Proyecto eliminado correctamente!")
        return redirect("proyectos")
