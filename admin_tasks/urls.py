from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls') ),
    path('dashboard/', include('dashboard.urls') ),
    path('proyectos/', include('proyectos.urls') ),
    path('proyectos/<int:id>/tareas/', include('tareas.urls') ),
    path('usuarios/', include('usuarios.urls') ),
    path('galeria/', include('galeria.urls') ),
    path('api/', include('api.urls') ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
