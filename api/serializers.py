from rest_framework import serializers
from proyectos.models import Proyecto
from tareas.models import Tarea
from galeria.models import Album, Foto
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    tareas = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Proyecto
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    fotos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
