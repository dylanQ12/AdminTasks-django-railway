from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from proyectos.models import Proyecto
from .models import Tarea

# Create your views here.
@login_required
def lista_tareas(request, id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, "list-tareas.html", {"proyecto": proyecto, "tareas": tareas})
    
    
@login_required
def crear_tareas(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("desc")
        if titulo and descripcion:
            tarea = Tarea(titulo=titulo, descripcion=descripcion, proyecto=proyecto)
            messages.success(request, '¡Tarea creada correctamente!')
            tarea.save()
            return redirect("tareas", id=id)
        else:
            messages.error(request, '¡El título de la tarea no puede estar vacío!')
            return redirect("tareas", id=id)

    tareas = proyecto.tareas.all()
    return render(
        request, "crear-tareas.html", {"proyecto": proyecto, "tareas": tareas}
    )


@login_required
def editar_tarea(request, id, tarea_id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("desc")
        completada = request.POST.get("completada", "off") == "on"
        if titulo:
            tarea.titulo = titulo
            tarea.descripcion = descripcion
            tarea.completada = completada
            tarea.save()
            messages.success(request, '¡Tarea actualizada correctamente!')
            return redirect("tareas", id=id)
        else:
            messages.error(request, '¡El título de la tarea no puede estar vacío!')
    context = {"proyecto": proyecto, "tarea": tarea}
    return render(request, "editar-tareas.html", context)


@login_required
def eliminar_tarea(request, id, tarea_id):
    proyecto = get_object_or_404(Proyecto, pk=id)
    if request.method == "POST":
        tarea = get_object_or_404(Tarea, pk=tarea_id)
        tarea.delete()
        messages.success(request, '¡Tarea eliminada correctamente!')
        return redirect("tareas", id=proyecto.id)
    return render(request, "list-tareas.html")
