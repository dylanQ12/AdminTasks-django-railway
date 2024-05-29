from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from proyectos.models import Proyecto
from tareas.models import Tarea
from galeria.models import Foto

User = get_user_model()


@login_required
def dashboardView(request):
    # Verificación de autenticación movida al principio
    if not request.user.is_authenticated:
        return redirect("login")

    # Obtener los contadores solo para el usuario autenticado
    proyectos_count = Proyecto.objects.filter(usuario=request.user).count()
    tareas_count = Tarea.objects.filter(
        proyecto__usuario=request.user, completada=0
    ).count()
    fotos_count = Foto.objects.filter(album__usuario=request.user).count()
    usuarios_count = (
        User.objects.filter(is_superuser=False).count()
        if request.user.is_superuser
        else None
    )

    # Counts
    context = {
        "proyectos_count": proyectos_count,
        "tareas_count": tareas_count,
        "fotos_count": fotos_count,
        "usuarios_count": usuarios_count,
    }

    return render(request, "main_dashboard.html", context)


@login_required
def lista_todas_tareas_usuario(request):
    proyectos_usuario = Proyecto.objects.filter(usuario=request.user)
    tareas_usuario = Tarea.objects.filter(proyecto__in=proyectos_usuario, completada=True)

    context = {
        "proyectos": proyectos_usuario,
        "tareas": tareas_usuario,
    }

    return render(request, "tareas-pendientes.html", context)


@login_required
def tareas_pendientes(request):
    proyectos_usuario = Proyecto.objects.filter(usuario=request.user)
    tareas_pendientes = Tarea.objects.filter(proyecto__in=proyectos_usuario, completada=False)
    data = {"tareas": tareas_pendientes}
    return render(request, 'tareas-pendientes.html', data)
    
