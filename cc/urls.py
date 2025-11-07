from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medico.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=Path(settings.BASE_DIR) / 'medico' / 'static')
