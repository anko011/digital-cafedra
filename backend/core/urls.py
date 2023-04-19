from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from apps.adresa.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dadata/', my_view),
    path('api/otcheti/', include('apps.otcheti.urls')),
    path('api/proekti/', include('apps.proekti.urls')),
    path('api/adresa/', include('apps.adresa.urls')),
    path('', TemplateView.as_view(template_name='index.html'))
]
if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
