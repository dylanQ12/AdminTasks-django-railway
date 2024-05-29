from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet, ProjectViewSet, AlbumViewSet, PhotoViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"tareas", TaskViewSet, basename="tarea")
router.register(r"proyectos", ProjectViewSet, basename="proyecto")
router.register(r"albums", AlbumViewSet, basename="album")
router.register(r"fotos", PhotoViewSet, basename="foto")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
