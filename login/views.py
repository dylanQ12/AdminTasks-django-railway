from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, f'¡Bienvenido de nuevo {user.first_name}!')
            return redirect("dashboard")
        else:
            messages.error(request, '¡Usuario o contraseña incorrectos!')
            return redirect("login")
    return render(request, "login.html")


# Vista del Logout para cerrar sesión.
def logoutView(request):
    logout(request)
    return redirect("/")
