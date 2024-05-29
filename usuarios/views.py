from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse

User = get_user_model()


# Create your views here.
@login_required
def listar_usuarios(request):
    superuser = request.user.is_superuser
    usuarios = User.objects.filter(is_superuser=False)
    if superuser:
        users = {"usuarios": usuarios}
        return render(request, "list-usuarios.html", users)
    return render(request, "list-usuarios.html")


@login_required
def crear_usuarios(request):
    if request.method == "POST":
        photo = request.POST.get("foto")
        first_name = request.POST.get("nombre")
        last_name = request.POST.get("apellido")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if photo and first_name and last_name and email and username and password:
            user = User(
                photo=photo,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.set_password(password)
            user.save()
            messages.success(request, "¡Usuario registrado correctamente!")
            return redirect(reverse("usuarios"))
    return render(request, "crear-usuario.html")


@login_required
def editar_usuarios(request, id):
    usuario = get_object_or_404(User, pk=id)

    if request.method == "POST":
        email = request.POST.get("email")
        es_admin = request.POST.get("esAdmin", "off") == "on"
        es_staff = request.POST.get("staff", "off") == "on"
        esta_activo = request.POST.get("activo", "off") == "on"

        if email:
            usuario.email = email
            usuario.is_superuser = es_admin
            usuario.is_staff = es_staff
            usuario.is_active = esta_activo

            usuario.save()
            messages.success(request, "¡Usuario actualizado correctamente!")
            return redirect(reverse("usuarios"))

    return render(request, "editar-usuario.html", {"usuario": usuario})


@login_required
def ver_perfil(request, id):
    usuario = get_object_or_404(User, pk=id)

    if request.method == "POST":
        foto = request.POST.get("foto")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if foto:
            usuario.photo = foto
            
        if password1 and password2:
            if password1 == password2:
                usuario.set_password(password1)
                update_session_auth_hash(request, usuario)  # Mantener la sesión activa
                login(request, usuario)  # Autenticar al usuario automáticamente
                usuario.save()
                messages.success(request, '¡Cambios guardados con éxito!')
                return redirect(reverse("dashboard"))
            else:
                messages.warning(request, '¡Las contraseñas no coinciden!')

    return render(request, "ver-perfil.html", {"usuario": usuario})
