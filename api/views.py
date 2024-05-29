from rest_framework import viewsets, status
from .serializers import (
    UserSerializer,
    TaskSerializer,
    ProjectSerializer,
    PhotoSerializer,
    AlbumSerializer,
)
from tareas.models import Tarea
from proyectos.models import Proyecto
from galeria.models import Album, Foto
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # Mostrar vista usuarios solo si esta autenticado y solo si es superuser.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return User.objects.all()
        else:
            return User.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            return super().list(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "No tienes permiso para ver esta vista."},
                status=status.HTTP_403_FORBIDDEN,
            )


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # Filtrar solo tareas del usuario autenticado.
    def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    # Filtrar proyectos del usuario autenticado.
    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    # Filtrar albums del usuario autenticado.
    def get_queryset(self):
        return Album.objects.filter(usuario=self.request.user)


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    # Filtrar fotos del usuario autenticado.
    def get_queryset(self):
        return Foto.objects.filter(album__usuario=self.request.user)
